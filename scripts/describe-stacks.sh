#!/usr/bin/env bash

STACK_NAME="$1"

aws cloudformation describe-stacks \
    --stack-name "${STACK_NAME}" \
    --profile buildingwebappswithdjango_mailape \
    --region us-west-2
