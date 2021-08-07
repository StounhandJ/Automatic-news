#!/bin/bash
#
# Author: Duye Chen
#

if [ -z $3 ]
then
    echo "Usage: ./run.sh [DOMAIN_NAME] [CLOUDFLARE_API_KEY] [CLOUDFLARE_EMAIL]"
    exit
fi

DOMAIN_NAME=$1
PATH=$PATH
DIR=`pwd`

########## Modify THIS SECTION #############
# MODE="staging"
CERTBOT_EMAIL="exempl@gmail.com"
CLOUDFLARE_API_KEY=$2
CLOUDFLARE_EMAIL=$3
############################################
docker build -t wildcard-certbot $DIR

docker run -it --rm \
    -v "$DIR/conf:/etc/letsencrypt" \
    -e DOMAIN_NAME=$DOMAIN_NAME \
    -e CERTBOT_EMAIL=$CERTBOT_EMAIL \
    -e CLOUDFLARE_API_KEY=$CLOUDFLARE_API_KEY \
    -e CLOUDFLARE_EMAIL=$CLOUDFLARE_EMAIL \
    -e MODE=$MODE \
    wildcard-certbot