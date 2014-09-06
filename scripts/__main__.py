#!/usr/bin/env python
#-*-coding:utf-8-*-

__author__ = 'ugursogukpinar'


import arguments
from VHCreator import VHCreator

def __main__():
    args = arguments.getArgs()

    if(not args.conf ):
        args.conf = "/usr/local/zend/apache2/conf/extra/httpd-vhosts.conf"

    __VHCreator = VHCreator(args.conf,args.directory)
    __VHCreator.addVirtualHost(args.servername)


if __name__ == "__main__":
    __main__()

