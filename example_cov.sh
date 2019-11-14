#!/usr/bin/env bash
export FLASK_ENV=test
export FLASK_DEBUG=0
export DATABASE_HOST_URL='Add connection string'
export N=10

coverage run --omit dev.settings --source "." -m py.test

coverage report
