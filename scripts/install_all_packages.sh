#!/usr/bin/env bash
set -e

sudo apt-get update
sudo apt install -y $(cat /mailape/ubuntu/packages.txt | grep -i '^[a-z]')

virtualenv -p $(which python3) /mailape/virtualenv
source /mailape/virtualenv/bin/activate

pip install -r /mailape/requirements.production.txt

sudo chown -R www-data:www-data /var/log/mailape \
    /etc/mailape \
    /var/run/celery \
    /var/log/celery

sudo usermod -a -G www-data ubuntu

sudo chmod -R ug+w /var/log/mailape \
    /etc/mailape \
    /var/run/celery \
    /var/log/celery