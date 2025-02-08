#!/bin/bash

# apply database migrations
python manage.py migrate --noinput

# collect static files
python manage.py collectstatic --noinput

# Start Gunicorn processes
echo Starting Gunicorn.
# -k uvicorn.workers.UvicornWorker \

exec gunicorn \
   --preload \
   --bind 0.0.0.0:8000 \
   --name app \
   --workers 3 \
   --forwarded-allow-ips="*" \
   --log-level=debug \
   --capture-output --enable-stdio-inheritance \
   --access-logfile '-' --error-logfile '-' \
   smwProject.wsgi:application
