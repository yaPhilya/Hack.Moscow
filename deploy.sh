#!/usr/bin/env bash

set -e

docker build -t strangeducttape/bluecat_backend .
docker push strangeducttape/bluecat_backend

scp ./docker-compose.yaml root@188.246.233.30:/app/backend

ssh root@188.246.233.30 "cd /app/backend && docker stack deploy --compose-file docker-compose.yaml backend"
