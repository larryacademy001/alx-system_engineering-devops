# fix apache configuration after returning a 500 error

exec { 'Fix 500 server error':
  command =>  "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
