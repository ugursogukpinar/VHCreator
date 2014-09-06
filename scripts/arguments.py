#!/usr/bin/env python
#-*-coding:utf-8-*-


__author__ = 'ugursogukpinar'

__TMPFILES__ = {
    'posix'  : '/tmp',
    'nt' : 'C:/tmp'
}

__ERRORS__ = {
    ''
}

import argparse,os,sys


class Arguments(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('servername',help='VirtualHost server name')
        parser.add_argument('directory', help='VirtualHost document root')
        parser.add_argument('-g','--git',help='Git repostiroy url to clone given directory',default=False)
        parser.add_argument('-cf','--conf',help='VirtualHosts configuration file path',default=False)
        parser.add_argument('-ho','--host', action="store_true" , help='With this option you can insert your server name into hosts file.',default=False)
        self.args = parser.parse_args()

    def getArgs(self):
        return self.args

    def getConfFilePath(self):
        try:
            tmpFile = open(__TMPFILES__[os.name],'r')
            confFilePath = tmpFile.readline().strip()
            self.args.conf = confFilePath

        except:
            self.returnError()



    def returnError(self,errorcode,**kwargs):
        errorStr = __ERRORS__[errorcode]

        if(len(kwargs)):
            for arg in kwargs:
                errorStr.format(arg)

        print errorStr
        sys.exit(1)
