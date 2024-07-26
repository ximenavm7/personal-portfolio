#!/bin/bash

# move to portfolio project
cd /root/personal-portfolio

# update git repo
git fetch && git reset origin/main --hard

#install new dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt
deactivate

# Obtain credentials from user
echo "MYSQL_USER: "
read user
echo "MYSQL_PASSWORD: "
read password
echo "MYSQL_DATABASE: "
read db
# Add extra information needed for Docker containers
echo "MY_ROOT_PASSWORD: "
read root

# Create new ENV file
touch .env
echo "URL=localhost:5000
MYSQL_HOST=localhost
MYSQL_USER=$user
MYSQL_PASSWORD=$password
MYSQL_DATABASE=$db
MY_ROOT_PASSWORD=$root
MARIADB_ROOT_PASSWORD=$root" > .env

# Restart myportfolio service
systemctl daemon-reload
systemctl restart myportfolio