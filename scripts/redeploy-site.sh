#!/bin/bash

# move to portfolio project
cd /root/personal-portfolio

# update git repo
git fetch && git reset origin/main --hard

# Spin containers down
docker compose -f docker-compose.prod.yml down

# Build and run containers
docker compose -f docker-compose.prod.yml up -d --build

# Check status of containers
status=$(docker ps -q)
if [ -n "$status" ]; then
  echo "Deployment Successful :)"
else
  echo "Containers are not running :("
fi
