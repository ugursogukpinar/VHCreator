#!/usr/bin/env python
#-*-coding:utf-8-*-


__AUTHOR__ = 'ugursogukpinar'

__TMPFILES__ = {
    'posix'  : '/tmp/VHCreator.conf',
    'nt' : 'C:/tmp/VHCreator.conf'
}

__ERRORS__ = {
    'conffilenotfound' : '{0} file not found. You have to give configuration file path.',
    'conffilecantwrite' : 'Default configuration could not save to {0}'
}

__VERSION__ = '0.1.2'

import argparse,os,sys


class Arguments(object):

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('servername',help='VirtualHost server name')
        parser.add_argument('directory', help='VirtualHost document root')
        parser.add_argument('-cf','--conf',help='VirtualHosts configuration file path.',default=False)
        parser.add_argument('-ho','--host', action="store_true" , help='With this option you can insert your server name into hosts file.',default=False)
        parser.add_argument('-v','--version',action="version", help="Version",version='%s' % (__VERSION__))
        # To next version
        # parser.add_argument('-g','--git',help='Git repostiroy url to clone given directory',default=False)
        # parser.add_argument('-a','--alias', help='You can give an alias virtual host',default=False)

        self.args = parser.parse_args()

        if(self.args.conf):
            self.setConfFile(self.args.conf)
        else:
            self.args.conf = self.getConfFilePath()

    def getArgs(self):
        return self.args

    def getConfFilePath(self):
        try:
            tmpFile = open(__TMPFILES__[os.name],'r')
            confFilePath = tmpFile.readline().strip()
            return confFilePath
        except:
            self.returnError('conffilenotfound',(__TMPFILES__[os.name]))


    def setConfFile(self,confFilePath):
        try:
            tmpFile = open(__TMPFILES__[os.name],'w')
            tmpFile.write(confFilePath)
            tmpFile.flush()
            tmpFile.close()
        except:
            print __ERRORS__['conffilecantwrite'].format(__TMPFILES__[os.name])



    def returnError(self,errorcode,**kwargs):
        errorStr = __ERRORS__[errorcode]

        if(len(kwargs)):
            for arg in kwargs:
                errorStr.format(arg)

        print errorStr
        sys.exit(1)
