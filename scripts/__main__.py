#!/usr/bin/env python
#-*-coding:utf-8-*-

__AUTHOR__ = 'ugursogukpinar'


from arguments import Arguments
from VHCreator import VHCreator
from git import Git

def main():
    __Arguments = Arguments()
    args = __Arguments.getArgs()

    __VHCreator = VHCreator(args.conf,args.directory)
    __VHCreator.addVirtualHost(args.servername)

    if(args.host):
        __VHCreator.addHostName(args.servername)

    if(args.repo):
        Git(args.repo,args.foldername,args.directory)

if __name__ == "__main__":
    main()

