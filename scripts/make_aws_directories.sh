#!/usr/bin/env bash
set -e

sudo mkdir -p /mailape/ubuntu \
    /mailape/apache \
    /mailape/django \
    /var/run/celery \
    /var/log/celery \
    /etc/mailape \
    /var/log/mailape

sudo chown -R ubuntu /mailape
