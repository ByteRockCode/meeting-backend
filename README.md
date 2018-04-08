# ByteRock Meeting Backend

[![Coverage Status](https://coveralls.io/repos/github/ByteRockCode/meeting-backend/badge.svg?branch=master)](https://coveralls.io/github/ByteRockCode/meeting-backend?branch=master)
[![Build Status](https://travis-ci.org/ByteRockCode/meeting-backend.svg?branch=master)](https://travis-ci.org/ByteRockCode/meeting-backend)

## Installation

```bash
brew update
brew install pyenv
pyenv install 3.6.2

mkdir -p ~/.envs
virtualenv -p ~/.pyenv/versions/3.6.2/bin/python ~/.envs/meeting

mkdir -p ~/Dev/ByteRock
cd ~/Dev/ByteRock
git clone git@github.com:ByteRockCode/meeting-backend.git

cd meeting-backend
sh scripts/database_build.sh
```
