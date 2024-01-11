#!/usr/bin/env bash
# Sets up the deployment of web static on web servers

# check if nginx is installed and if not installs it
if ! nginx -v &> /dev/null
then
	sudo apt update -y
	sudo apt install nginx -y
fi
# Creates specified directories using -p flag to check if they exists first

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Creates a fake HTML file to test nginx configuration
html_file="/data/web_static/releases/test/index.html"
fake_html="<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>"
echo "$fake_html" | sudo tee "$html_file" > /dev/null

# Force create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of a folder to a user
sudo chown -R ubuntu:ubuntu /data/

# Configuring nginx to serve the content of hbnb_static
nginx_config="/etc/nginx/sites-available/default"
hbnb_index="\\
\tlocation /hbnb_static {\\
\t\t alias /data/web_static/current/;\\
\t}"
sudo sed -i '/server_name _;/a '"$hbnb_index"'' "$nginx_config"

# Restarting nginx
sudo service nginx restart
