#!/bin/bash

rm config/db.sqlite3
python manage.py migrate
sh scripts/load_fixtures.sh
