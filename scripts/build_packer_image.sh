#!/usr/bin/env bash

cd packer

packer build \
    -var "aws_access_key=$AWS_ACCESS_KEY" \
    -var "aws_secret_key=$AWS_SECRET_KEY" \
    -var "django_db_password=$DB_PASSWORD" \
    -var "django_db_host=$DB_HOST" \
    -var "django_secret=$DJANGO_SECRET" \
    -var "email_host=$EMAIL_HOST" \
    -var "email_host_password=$EMAIL_HOST_PASSWORD" \
    -var "web_domain=$WEB_DOMAIN" \
    web_worker.json
