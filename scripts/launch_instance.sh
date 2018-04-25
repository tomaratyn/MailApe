#!/usr/bin/env bash

aws ec2 run-instances \
    --image-id ami-ed6af595 \
    --count 1 \
    --instance-type t2.micro \
    --key-name tom-mbp-building-django-with-django \
    --security-group-ids "ssh-access" "web-access" \
    --region us-west-2 \
    --profile buildingwebappswithdjango_mailape
