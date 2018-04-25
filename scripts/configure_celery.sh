#!/usr/bin/env bash

sudo ln -s /mailape/ubuntu/celery.service /etc/systemd/system/celery.service
sudo ln -s /mailape/ubuntu/celery.service /etc/systemd/system/multi-user.target.wants/celery.service
sudo ln -s /mailape/ubuntu/tmpfiles-celery.conf /etc/tmpfiles.d/celery.conf