# Using puppet to configure two web servers

html_file = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

package { 'nginx':
  ensure => installed,
}
exec {'configure nginx':
    command  => 'sudo mkdir -p /data/web_static/releases/test/ &&sudo mkdir -p /data/web_static/shared/ &&
                sudo echo $html_file > /data/web_static/releases/test/index.html &&
                sudo ln -sf /data/web_static/releases/test/ /data/web_static/current &&
                sudo chown -R ubuntu:ubuntu /data/ &&
                new_update="\\\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" &&
                sudo sed -i "55i $new_update" /etc/nginx/sites-available/default &&
                sudo service nginx restart',
    provider => 'shell',
}
