#!/bin/bash
# scripts/dump_fixtures.sh

dumpdata="python manage.py dumpdata --indent 2"

# backend
$dumpdata auth.user > backend/fixtures/auth.user.json

# backend/scoreboard
$dumpdata scoreboard.kattishandle > \
  backend/scoreboard/fixtures/kattishandle.json
