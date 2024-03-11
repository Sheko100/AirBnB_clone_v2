# Setting up the web server to the deployemnt of web_static
exec { 'apt update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx']
}
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
}
file { 'config':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  require => Package['nginx']
}
exec { 'shared':
  command => '/usr/bin/mkdir -p /data/web_static/shared/',
}
exec { 'releases':
  command => '/usr/bin/mkdir -p /data/web_static/releases/test/',
  before  => File['index']
}

$html = "<!doctype html>\n<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHello Earth!\n\t</body>\n</html>"

file { 'index':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  content => $html
}

exec { 'remove old symbolic':
  command => 'rm -r /data/web_static/current',
  onlyif  => 'test -d /data/web_static/current',
  before  => File['symbolic']
}

exec { 'symbolic':
  command => 'ln -s /data/web_static/releases/test/ /data/web_static/current',
  require => Exec['releases']
}

exec { 'change owner and group':
  command => 'chown -R ubuntu:ubuntu /data/',
  require => [
    Exec['shared'],
    Exec['releases']
  ]
}

$cfg_path = '/etc/nginx/sites-enabled/default"'
$hbnb_alias = 'hbnb_static {\n\t\t\talias /data/web_static/current;\n\t\t}'

exec { 'Add /hbnb_static alias':
  command => '/usr/bin/sed -i -r "s|^(\tlocation /).*|&\n\n\t\1$hbnb_alias|" "$cfg_path"',
  onlyif  => '/usr/bin/grep -q "location /hbnb_static" "$cfg_path"',
  require => File['config']
}
exec { 'restart web server':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}
