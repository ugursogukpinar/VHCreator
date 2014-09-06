__author__ = 'ugursogukpinar'


import parser
from VHCreator import VHCreator

def __main__():
    args = parser.getArgs()

    if(not args.conf ):
        args.conf = "/usr/local/zend/apache2/conf/extra/httpd-vhosts.conf"

    __VHCreator = VHCreator(args.conf,args.directory)
    __VHCreator.addVirtualHost(args.servername)


if __name__ == "__main__":
    __main__()

