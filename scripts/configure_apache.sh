#!/usr/bin/env bash

sudo rm /etc/apache2/sites-enabled/*
sudo ln -s /mailape/apache/mailape.apache.conf /etc/apache2/sites-enabled/000-mailape.conf
