#!/usr/bin/env bash

psql -v ON_ERROR_STOP=1 postgresql://$USER:$PASSWORD@$HOST/postgres <<-EOSQL
    CREATE DATABASE mailape;
    CREATE USER mailape;
    GRANT ALL ON DATABASE mailape to "mailape";
    ALTER USER mailape PASSWORD '$DJANGO_DB_PASSWORD';
    ALTER USER mailape CREATEDB;
EOSQL
