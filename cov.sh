#!/usr/bin/env bash
export M_APP_SETTINGS=$(pwd)/dev.settings
export FLASK_ENV=test
export FLASK_DEBUG=0
coverage run --source "." -m py.test

coverage report