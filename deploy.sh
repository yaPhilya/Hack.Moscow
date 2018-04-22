#!/usr/bin/env bash

set -e

docker build -t strangeducttape/bluecat_backend .
docker push strangeducttape/bluecat_backend
