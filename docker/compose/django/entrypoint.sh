#!/bin/bash

set -e

if [[ $3 = "runserver" ]]; then
  yes "yes" | python /app/backend/manage.py migrate
fi

exec "$@"
