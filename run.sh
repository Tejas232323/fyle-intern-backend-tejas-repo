#!/bin/bash

# to stop on first error
set -e

# Delete older .pyc files
# find . -type d \( -name env -o -name venv  \) -prune -false -o -name "*.pyc" -exec rm -rf {} \;

# Run required migrations
export FLASK_APP=core/server.py

# Only run migration commands if needed
if [ ! -d "core/migrations/versions" ]; then
   flask db init -d core/migrations/
fi
flask db migrate -m "Initial migration." -d core/migrations/
flask db upgrade -d core/migrations/

# Run server with Waitress
waitress-serve --host=127.0.0.1 --port=8080 core.server:app
