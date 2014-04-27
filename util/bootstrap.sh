#!/bin/bash

# usage: ./bootstrap.sh dev|prod


default=prod
deploy=${1:-$default}

# TODO:
# - create venv if not there
# - install dev dependencies


# link to UI
echo linking Django app to Yeoman UI

echo "----> $deploy layout"
rm -f static
if [[ $deploy = "dev" ]]; then
    echo "warning: dev layout not yet working, use prod"
    ln -s app static
elif [[ $deploy = "prod" ]]; then
    ln -s prod/static static
fi
