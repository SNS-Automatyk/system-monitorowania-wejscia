# syntax=docker/dockerfile:1.3


# ----- DJANGO -----
FROM python:3.12-slim as django

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app


COPY ./ .

RUN mkdir -p ./assets
RUN mkdir -p ./logs 
RUN chmod 755 .  
RUN chmod -R +x ./scripts
# RUN pip3 install --no-cache-dir -r ./requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r ./requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install gunicorn psycopg2-binary

# CMD ["./scripts/docker-entrypoint-django.sh", "-n"]