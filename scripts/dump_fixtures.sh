#!/bin/bash
# scripts/dump_fixtures.sh

dumpdata="python manage.py dumpdata --indent 2"

# backend
$dumpdata auth.user > backend/fixtures/auth.user.json

# backend/about
$dumpdata about.progteamdesc > backend/about/fixtures/progteamdesc.json
$dumpdata about.meetinginfo > backend/about/fixtures/meetinginfo.json
$dumpdata about.officerinfo > backend/about/fixtures/officerinfo.json

# backend/scoreboard
$dumpdata scoreboard.kattishandle > \
  backend/scoreboard/fixtures/kattishandle.json
