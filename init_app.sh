#!/bin/bash

cd /geekshop;
export DJANGO_PRODUCTION=1;
python ./manage.py migrate;
python ./manage.py collectstatic --noinput;

echo "gunicorn --access-logfile - --env DJANGO_PRODUCTION=1 --bind unix:/var/run/geekshop/geekshop.sock --workers 3 geekshop.wsgi:application" | su django -G www-data 
