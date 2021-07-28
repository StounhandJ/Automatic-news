#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

docker-compose down

git fetch --all
git reset --hard origin/master

chmod +x data/init-letsencrypt.sh
chmod +x run.sh
chmod +x restart.sh

docker-compose up --build -d