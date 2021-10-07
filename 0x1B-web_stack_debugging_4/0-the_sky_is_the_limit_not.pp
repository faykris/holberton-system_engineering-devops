# Fix failed requests from 962 to 0 - change worker_processes value: 4 to 7
exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/' /etc/nginx/nginx.conf; sudo service nginx restart",
  provider => shell,
}
