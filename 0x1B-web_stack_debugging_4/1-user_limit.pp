# Fix holberton user limits - comment two lines which says holberton 
exec { 'change-os-configuration-for-holberton-user':
  command => "sed -i 's/holberton/# holberton/g' /etc/security/limits.conf",
  provider => shell,
}
