#!/bin/bash

python manage.py migrate
sh scripts/load_fixtures.sh
