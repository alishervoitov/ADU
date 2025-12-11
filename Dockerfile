FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Logs, static va media papkalarni yaratish
RUN mkdir -p /app/logs /app/staticfiles /app/media

COPY requirements/production.txt requirements/base.txt ./
RUN pip install --no-cache-dir -r production.txt

COPY . .

# Django collectstatic
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Production WSGI server
CMD python manage.py migrate && \
    gunicorn \
    --workers 4 \
    --bind 0.0.0.0:8000 \
    --access-logfile /app/logs/access.log \
    --error-logfile /app/logs/error.log \
    core.wsgi:application