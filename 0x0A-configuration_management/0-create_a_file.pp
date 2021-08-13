# Create a file in /tnp name holberton.
file {'/tmp/holberton':
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  mode    => '0744'
}
