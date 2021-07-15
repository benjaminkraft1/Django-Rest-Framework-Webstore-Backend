#!/bin/bash

set -e
set -x

unset http_proxy && unset https_proxy unset HTTP_PROXY unset HTTPS_PROXY

# install dependencies
echo "-- installing system dependencies --"
sudo apt update && sudo apt install build-essential libsasl2-dev python3-dev libldap2-dev libssl-dev binutils libproj-dev gdal-bin libgeoip1 python-gdal nodejs python-virtualenv -y

# create the logfile and make it readable
echo "-- creating log files --"
sudo touch /var/log/storefront/django.log
sudo chmod 777 /var/log/storefront/django.log

# create the virtual environment
echo "-- creating the virtual env --"

# setuptools appear to be problematic on create of the virtual env
virtualenv -p python3.6 storefront-env --no-setuptools
# activate the virtual environment
echo "-- activate the virtual environment --"
unset PYTHONPATH
source storefront-env/bin/activate

# upgrade pip
echo "-- upgrade pip --"
pip3 install --upgrade pip

# install setuptools (inside the virtenv, its no problem)
pip3 install setuptools

# install dependencies
echo "-- installing dependencies --"
pip3 install -r requirements.txt
