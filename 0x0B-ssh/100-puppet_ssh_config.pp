# 4. Client configuration file (w/ Puppet)
# change configuration file - connect without using a password
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config':
  path => '/usr/bin/',
}
