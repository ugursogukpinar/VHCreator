#!/usr/bin/env python
#-*-coding:utf-8-*-


__AUTHOR__ = 'ugursogukpinar'

__TMPFILES__ = {
    'posix'  : '/tmp/VHCreator/VHCreator.conf',
    'nt' : 'C:/tmp/VHCreator/VHCreator.conf'
}

__ERRORS__ = {
    'conffilenotfound' : '{0} file not found. You have to give configuration file path.',
    'conffilecantwrite' : 'Default configuration could not save to {0}',
    'requiredfoldername' : 'You must give foldername with -f operator to clone directory'
}

__VERSION__ = '0.1.3'

import argparse,os,sys


class Arguments(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('servername',help='VirtualHost server name')
        parser.add_argument('directory', help='VirtualHost document root')
        parser.add_argument('-cf','--conf',help='VirtualHosts configuration file path.',default=False)
        parser.add_argument('-ho','--host', action="store_true" , help='With this option you can insert your server name into hosts file.',default=False)
        parser.add_argument('-v','--version',action="version", help="Version",version='%s' % (__VERSION__))

        parser.add_argument('-r','--repo',help='Git repository url to clone given directory',default=False)
        parser.add_argument('-f','--foldername',help="Foldername define which folder will use on cloning.")

        self.args = parser.parse_args()

        if(self.args.conf):
            self.setConfFile(self.args.conf)
        else:
            self.args.conf = self.getConfFilePath()

        if(self.args.repo):
            if(not self.args.foldername):
                self.returnError('requiredfoldername')


    def getArgs(self):
        return self.args

    def getConfFilePath(self):
        try:
            tmpFile = open(__TMPFILES__[os.name],'r')
            confFilePath = tmpFile.readline().strip()
            return confFilePath
        except:
            self.returnError('conffilenotfound',list(__TMPFILES__[os.name]))


    def setConfFile(self,confFilePath):
        try:
            tmpFile = open(__TMPFILES__[os.name],'w')
            tmpFile.write(confFilePath)
            tmpFile.close()
        except:
            print __ERRORS__['conffilecantwrite'].format(__TMPFILES__[os.name])



    def returnError(self,errorcode,*args):
        errorStr = __ERRORS__[errorcode]

        if(len(args)):
            for arg in args:
                errorStr.format(arg)

        print errorStr
        sys.exit(2) #Return with exit
