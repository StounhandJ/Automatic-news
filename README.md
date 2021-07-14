# Automatic-news
[[EN]](README.md) [[RU]](README_RU.md)
#### Automatic news site, with a separate parser of new publications on other sites. With the launch of the entire project by two teams
****
## Dependencies:
1. [Docker](https://www.docker.com/)
1. [docker-compose](https://github.com/docker/compose)
## Launch:
1. Build the project using Docker, being in the root directory `docker-compose build` (once)
1. Launch the `docker-compose up-d` project
****
## Additional:
After the launch, the site will be available at `localhost:8080`. The parser will check the sites for new articles every 10 minutes, after checking they will immediately be displayed on the site.