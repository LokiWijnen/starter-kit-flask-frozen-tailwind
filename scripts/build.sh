#!/bin/bash

export ENVIRONMENT="${ENVIRONMENT:-production}"

rm -rf project/build project/static/.webassets-cache project/static/dist

python3 app.py build
