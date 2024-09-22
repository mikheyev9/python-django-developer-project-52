#!/bin/sh
envsubst '${SERVER_HOST}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

nginx -g 'daemon off;'