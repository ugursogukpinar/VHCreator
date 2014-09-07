===========
VHCreator
===========

VHCreator created to manage virtual hosts. For now you can add virtual host with one simply act like:

    $vhcreator <servername> <directory> -ho -cf /etc/apache2/sites-available/000-default.conf

Options
=========
In addition , you can use this options.

* -h HELP

* -cf This define your server virtual hosts configuration file path
  to add virtual host. In first use you have to define it then it will be used
  on other sessions.
* -ho With this option , you can add given <servername> to operating system hosts file
      automaticaly.

In future
-------------
1. Added hosts could be deleted with given alias.

2. User can clone a git repository to given directory.


Contributors
-------------

1. Uğur Soğukpınar