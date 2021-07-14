FROM composer as composer
COPY . /app
RUN composer install --ignore-platform-reqs --no-scripts


FROM php:fpm
WORKDIR /var/www/root/


RUN docker-php-ext-install pdo pdo_mysql
RUN pecl install mongodb && docker-php-ext-enable mongodb

COPY . /var/www/root
COPY --from=composer /app/vendor /var/www/root/vendor

EXPOSE 8000
CMD bash -c "php -S 0.0.0.0:8000 -t public"