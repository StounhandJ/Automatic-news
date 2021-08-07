#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

loadEnv() {
  local envFile="${1?Missing environment file}"
  local environmentAsArray variableDeclaration
  mapfile environmentAsArray < <(
    grep --invert-match '^#' "${envFile}" \
      | grep --invert-match '^\s*$'
  ) # Uses grep to remove commented and blank lines
  for variableDeclaration in "${environmentAsArray[@]}"; do
    export "${variableDeclaration//[$'\r\n']}" # The substitution removes the line breaks
  done
}

loadEnv .env

echo "Collecting a project..."
docker-compose build

echo "Granting rights to files..."
chmod +x data/init-letsencrypt.sh
chmod +x data/certbot/run.sh
chmod +x data/certbot/gen-ssl.sh
chmod +x restart.sh

echo "Getting a wildcard certificate..."
docker build -t wildcard-certbot data/certbot/
./data/certbot/run.sh $DOMAIN $CLOUDFLARE_API_KEY $CLOUDFLARE_EMAIL

echo "Reboot..."
docker-compose down
docker-compose up -d