#!/bin/bash
project_path=`pwd`
sudo ln -s $project_path/nginx/mighty.conf /etc/nginx/sites-enabled/
sudo mkdir /var/www/mighty
