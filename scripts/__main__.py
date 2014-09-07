#!/usr/bin/env python
#-*-coding:utf-8-*-

__author__ = 'ugursogukpinar'


from arguments import Arguments
from VHCreator import VHCreator

def __main__():
    __Arguments = Arguments()
    args = __Arguments.getArgs()

    __VHCreator = VHCreator(args.conf,args.directory)
    __VHCreator.addVirtualHost(args.servername)

    if(args.host):
        __VHCreator.addHostName(args.servername)

if __name__ == "__main__":
    __main__()

