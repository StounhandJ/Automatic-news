FROM composer as composer
COPY composer.* /app/
RUN composer install --ignore-platform-reqs --no-scripts

FROM php:fpm

COPY composer.lock composer.json /var/www/

WORKDIR /var/www

RUN pecl install mongodb && docker-php-ext-enable mongodb

RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

COPY --chown=www:www . /var/www
COPY --from=composer /app/vendor /var/www/vendor

USER www

EXPOSE 9000
CMD ["php-fpm"]
