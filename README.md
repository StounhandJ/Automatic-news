# Automatic-news
[EN] [[RU]](README_RU.md)
#### Automatic news site, with a separate parser of new publications on other sites. There is also an automatic issuance of an SSL certificate.
****
## Dependencies:
1. [Docker](https://www.docker.com/)
1. [docker-compose](https://github.com/docker/compose)
## Launch:
1. In the file [.env](.env) write your domain to the DOMAIN variable
1. `chmod +x run.sh` Grant rights to execute the script
1. `./run.sh` Run the project
****
## Additional:
To restart the project and get new updates, write `./restart.sh`.  
The parser will check the sites for new articles every 10 minutes, after checking they will immediately be displayed on the site.