#!/bin/bash

service cron start
service supervisor start
php-fpm
