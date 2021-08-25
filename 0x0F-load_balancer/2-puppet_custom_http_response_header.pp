# 2. Add a custom HTTP header with Puppet
exec { 'apt-get update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

exec {'nginx install':
  command  => 'sudo apt-get -y install nginx && sudo ufw allow "Nginx HTTP"',
  provider => shell,
}

exec {'create index':
  command  => 'echo "Holberton School" > index.html && sudo mv index.html /var/www/html/',
  provider => shell,
}

exec {'nginx start':
  command  => 'sudo service nginx start',
  provider => shell,
}

exec { 'add X-Served-By':
  command  => 'sudo sed -i "/displaying a 404./a add_header X-Served-By \$hostname always;" /etc/nginx/sites-available/default',
  provider => shell,
}

exec { 'nginx restart':
  command  => 'sudo service nginx restart',
  provider => shell,
}
