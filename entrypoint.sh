#!/bin/bash
set -e

# Migrations, collectstatic, etc.
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Démarrer Gunicorn
exec gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000 &
nginx -g "daemon off;"
