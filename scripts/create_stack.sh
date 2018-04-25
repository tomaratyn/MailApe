#!/usr/bin/env bash

NAME="$1"
STACK_PATH="$2"
PARAMETERS="$3"
MORE_PARAMTERS="$4"

aws cloudformation create-stack \
    --stack-name "$NAME" \
    --template-body "file://$STACK_PATH" \
    --capabilities CAPABILITY_NAMED_IAM \
    --profile buildingwebappswithdjango_mailape \
    --parameters "$PARAMETERS" \
    --region us-west-2
