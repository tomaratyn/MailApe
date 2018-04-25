#!/usr/bin/env bash

docker run -p 5432:5432 \
    -e DJANGO_DB_NAME=mailape \
    -e DJANGO_DB_USER=mailape \
    -e DJANGO_DB_PASSWORD=development \
    -e POSTGRES_PASSWORD=development \
    -d \
    --name mailape-postgres \
    tomaratyn/mailape_postgres