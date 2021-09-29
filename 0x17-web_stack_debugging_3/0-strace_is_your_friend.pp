# 0. Strace is your friend
# replace all phpp by php extension on a file 'wp-settings.php'
exec { 'fix-wordpress':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php; sudo service apache2 restart',
  provider => shell,
}
