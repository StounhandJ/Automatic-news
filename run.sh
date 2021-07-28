#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

docker-compose build

chmod +x data/init-letsencrypt.sh
chmod +x restart.sh

./data/init-letsencrypt.sh

docker-compose down

docker-compose up -d