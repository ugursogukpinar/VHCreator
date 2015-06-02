####VHCreator

VHCreator created to manage virtual hosts. For now you can add virtual host with one simply act like:

    $ vhcreator <servername> <directory> -ho -cf /etc/apache2/sites-available/000-default.conf

####Installation

```bash
$ [sudo] pip install vhcreator
```


####Options

- -h HELP

- -cf This define your server virtual hosts configuration file path
  to add virtual host. In first use you have to define it then it will use
  on other sessions.

- -ho With this option , you can add given <servername> to operating system hosts file
      automaticaly.
- -r Git repository url to clone given directory

- -f Foldername define which folder will use on cloning.

####In future

- Added hosts could be deleted with given alias.
