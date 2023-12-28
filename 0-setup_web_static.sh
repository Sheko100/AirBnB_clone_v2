#!/usr/bin/env bash
# sets up the web servers for the doployment of web_static
apt-get update > /dev/null
apt-get -y install nginx > /dev/null
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
html="<!doctype html>\n<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHello Earth!\n\t</body>\n</html>"
echo -e "$html" > /data/web_static/releases/test/index.html
test -d /data/web_static/current && rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
cfg_path="/etc/nginx/sites-available/default"
hbnb_alias="\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current/;\n\t\t}"
grep -q "location /hbnb_static" "$cfg_path" || sed -i "s|^\tlocation / {|\tlocation / {\n\n$hbnb_alias|" "$cfg_path"
service nginx reload
