#!/usr/bin/env bash

NAME="$1"
STACK_PATH="$2"
PARAMETERS="$3"
MORE_PARAMETERS="$4"

aws cloudformation update-stack \
    --stack-name "$NAME" \
    --capabilities CAPABILITY_NAMED_IAM \
    --template-body "file://$STACK_PATH" \
    --profile buildingwebappswithdjango_mailape \
    --parameters "$PARAMETERS" "$MORE_PARAMETERS" \
    --region us-west-2
