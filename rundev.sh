#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=development
export M_APP_SETTINGS=$(pwd)/dev.settings

flask run --host=0.0.0.0 --port 5001
