FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies in isolated layer
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt
FROM python:3.11-slim AS production
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
COPY templates/ templates/
COPY static/ static/
COPY .env .
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 5000
ENV FLASK_APP=app.py \
    FLASK_DEBUG=false \
    PORT=5000 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Run with gunicorn for production
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "app:app"]
