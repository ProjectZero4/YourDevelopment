#!/bin/bash

chown -R www-data:1000 /var/www/html
chmod -R 775 /var/www/html
if [ -f /var/www/html/artisan ]; then
  php /var/www/html/artisan migrate --force
  { crontab -l; echo "* * * * * cd /var/www/html && php artisan schedule:run >> /dev/null 2>&1"; } | crontab -
fi
service nginx start
service cron start
service supervisor start
php-fpm
