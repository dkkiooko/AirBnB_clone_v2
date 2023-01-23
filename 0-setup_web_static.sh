#!/usr/bin/env bash
# set up web servers for deployment of webstatic
WHERE="/etc/nginx/sites-available/default"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
cp /etc/nginx/sites-available/default{,.orig}
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "this is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" $WHERE
service nginx restart
