exec { 'kill_killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/usr/bin', '/bin'],
  onlyif      => 'pgrep -f killmenow',
}

