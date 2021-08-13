# Create a manifest that kills a process named killmenow
exec { 'pkill -15 killmenow':
  path    => ['/usr/bin', '/usr/sbin',],
}
