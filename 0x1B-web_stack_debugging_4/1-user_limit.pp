# Change the OS configuration so that it is possible to login in.

exec { 'increase-hard-file-limit-for-holberton-user':
  command => "echo 'holberton hard nofile 50000' >> /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => "echo 'holberton soft nofile 50000' >> /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}