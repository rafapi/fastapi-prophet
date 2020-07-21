#!/usr/bin/env sh

echo "Waiting for database..."

while ! nc -z prophet-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"
