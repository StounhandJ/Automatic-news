FROM php:fpm

RUN docker-php-ext-install pdo pdo_mysql
RUN pecl install mongodb && docker-php-ext-enable mongodb