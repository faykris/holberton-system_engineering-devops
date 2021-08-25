# 2. Add a custom HTTP header with Puppet
exec { 'nginx install':
  command  => 'apt-get -y update; apt-get -y install nginx; sudo sed -i "/displaying a 404./a add_header X-Served-By \$hostname always;" /etc/nginx/sites-available/default; service nginx restart',
  provider => shell,
}
