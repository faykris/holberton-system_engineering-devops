file_line { 'Pass_Auth_no':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
file_line { 'Iden_File_Holberton':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton',
}
