### Hexlet tests and linter status:
[![Actions Status](https://github.com/mikheyev9/python-django-developer-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mikheyev9/python-django-developer-project-52/actions)

установка сертификатов
sudo mkdir -p /var/www/certbot
sudo chown -R $USER:$USER /var/www/certbot
sudo chmod -R 755 /var/www/certbot

sudo certbot certonly --webroot -w /var/www/certbot -d