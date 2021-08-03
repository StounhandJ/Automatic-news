FROM php:fpm

COPY composer.lock composer.json /var/www/

WORKDIR /var/www

RUN pecl install mongodb && docker-php-ext-enable mongodb
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

COPY --chown=www:www . /var/www

USER www

EXPOSE 9000
CMD ["php-fpm"]
