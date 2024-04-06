#!/bin/sh
set -e

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python3 manage.py migrate

# Start NGINX in the background
echo "Starting NGINX..."
nginx &

# Start Gunicorn in the foreground to keep the container running
echo "Starting Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
