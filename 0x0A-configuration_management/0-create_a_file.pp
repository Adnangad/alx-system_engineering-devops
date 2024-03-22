# This puppet creates a file and assigns to it users and permissions
file { '/tmp/school':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet"
}
