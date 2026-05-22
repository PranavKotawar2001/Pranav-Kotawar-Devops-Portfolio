FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS production
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
COPY templates/ templates/
COPY static/ static/
RUN chown -R appuser:appuser /app
USER appuser
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "app:app"]
