#!/bin/bash
# scripts/test_frontend.sh

CI=true npm test -C frontend && \
# Run linter
npm run lint -C frontend
