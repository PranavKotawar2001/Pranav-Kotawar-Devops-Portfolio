# ─────────────────────────────────────────────
# Stage 1: Builder — install dependencies
# ─────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies in isolated layer
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

# ─────────────────────────────────────────────
# Stage 2: Production — lean final image
# ─────────────────────────────────────────────
FROM python:3.11-slim AS production

# Security: create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application source
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Copy env (override with K8s secrets/configmap in production)
COPY .env .

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/')" || exit 1

# Environment defaults
ENV FLASK_APP=app.py \
    FLASK_DEBUG=false \
    PORT=5000 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Run with gunicorn for production
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "app:app"]
