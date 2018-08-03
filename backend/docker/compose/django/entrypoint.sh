#!/bin/bash

set -e

if [[ $3 = "runserver" ]]; then
  yes "yes" | python /app/manage.py migrate
fi

exec "$@"
