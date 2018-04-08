#!/bin/bash

rm config/db.sqlite3
sh scripts/database_build.sh
sh scripts/load_fixtures.sh
