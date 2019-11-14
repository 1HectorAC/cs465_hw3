#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=development
export DATABASE_HOST_URL='Add connection string'
export N=10

flask run --host=0.0.0.0 --port $@
