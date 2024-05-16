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

file { '/data/web_static/releases/test':
  ensure => directory,
  before => File['/data/web_static/shared', '/data/web_static/releases/test/index.html'],
}

file { '/data/web_static/shared':
  ensure => directory,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => $html_content,
  require => File['/data/web_static/releases/test'],
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file_line { 'nginx_hbnb_static_config':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => '        location /hbnb_static {',
  after  => '    server_name _;',
}

exec { 'nginx_restart':
  command     => 'service nginx restart',
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
  subscribe   => File_line['nginx_hbnb_static_config'],
}
