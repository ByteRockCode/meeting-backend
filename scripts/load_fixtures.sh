#!/bin/sh

python manage.py loaddata --app profiles users
python manage.py loaddata --app companies companies
python manage.py loaddata --app profiles profiles
python manage.py loaddata --app meetings meetings
python manage.py loaddata --app meetings guests
