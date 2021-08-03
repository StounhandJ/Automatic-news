#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

docker-compose down

mv .env .env.example

git fetch --all
git reset --hard origin/master

mv .env.example .env
mv site/.env.example site/.env
chmod +x data/init-letsencrypt.sh
chmod +x run.sh
chmod +x restart.sh

docker-compose up --build -d