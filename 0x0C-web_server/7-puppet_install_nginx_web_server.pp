#!/usr/bin/env bash
# Script to install nginx using puppet

package { 'nginx':
  ensure => 'installed',
}

exec { 'install':
  command  => 'sudo apt-get update && sudo apt-get -y install nginx',
  provider => 'shell',
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default':
  content => "server {\n  listen 80 default_server;\n  location /redirect_me {\n    return 301 https://blog.ehoneahobed.com/;\n  }\n}\n",
}

exec { 'nginx-restart':
  command  => 'sudo service nginx restart',
  require  => [Package['nginx'], File['/etc/nginx/sites-available/default']],
  subscribe => File['/etc/nginx/sites-available/default'],
  refreshonly => true,
  provider => 'shell',
}