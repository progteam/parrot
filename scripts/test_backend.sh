#!/bin/bash
# scripts/test_backend.sh

# We need to include those variables for testing PRs since Travis cannot
# disclose the secure branch environment variables. Read more at
#   https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml
export PARROT_CDN_HOST='https://cdn.progteam.org'
# If PARROT_ENV is not production, use the test environment
if [ -z "$PARROT_ENV" ] || [ "$PARROT_ENV" != 'production' ] ; then
  export PARROT_ENV='test'
fi
echo "Testing backend using $PARROT_ENV environment..."

# Create DB migrations before running the tests
python manage.py migrate && \
python manage.py collectstatic --noinput && \
python manage.py test && \
# Run linter and exclude directories: penv, migrations, and node_modules
find . -type d \( \
  -name migrations -o \
  -name node_modules -o \
  -name penv \
\) -prune -o -name "*.py" -print \
| xargs pylint --load-plugins pylint_django
