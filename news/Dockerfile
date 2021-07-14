FROM composer as composer
COPY . /app
RUN composer install --ignore-platform-reqs --no-scripts


FROM php:fpm
WORKDIR /var/www


RUN docker-php-ext-install pdo pdo_mysql
RUN pecl install mongodb && docker-php-ext-enable mongodb

COPY . /var/www
COPY --from=composer /app/vendor /var/www/vendor

RUN chown -R www-data:www-data /var/www

WORKDIR /var/www/public
EXPOSE 9000
CMD ["php-fpm"]
#CMD bash -c "php -S 0.0.0.0:8000 -t public"