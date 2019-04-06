#!/bin/bash
# scripts/load_fixtures.sh

if [ "$PARROT_ENV" = "production" ] ; then
  echo -e "\e[01;31mError: This script should never run in the production" \
    "environment\e[0m"
  exit 1
fi
python manage.py migrate
find backend -name *.json | grep fixtures | xargs python manage.py loaddata
