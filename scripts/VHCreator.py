#!/usr/bin/env python
#-*-coding:utf-8-*-
__AUTHOR__ = 'ugursogukpinar'


import os,sys

__ERRORS__ = {
    'notfound' : '\n{} file not found.',
    'notopen' : '\n{} can\'t open. Try with root priviliges.'
}

__VIRTUALHOST__ = '''\n
    # Added with VHCreator
    # Alias of VirtualHost \'{3}\'
    <VirtualHost *:{0}>
        DocumentRoot {1}
        ServerName {2}
    </VirtualHost>
\n'''

__ETCHOSTS__ = {
    'posix' : '/etc/hosts',
    'nt' : 'C:\Windows\System32\Drivers\etc\hosts'
}

__HOSTNAME__ = '\n{0}         {1}\n'

class VHCreator(object):
    def __init__(self,configFilePath,virtualHostDirectory):
        self.configFilePath = configFilePath
        self.virtualHostDirectory = virtualHostDirectory
        self.checkPathsExist(self.configFilePath)

    # Check configuration file exist
    def checkPathsExist(self,filePath):
        if(os.path.isfile(filePath) == False):
            print __ERRORS__['notfound'].format(filePath)
            sys.exit(2) #  Return with exit


    # Add virtual host script to conf file
    def addVirtualHost(self,serverName,serverPort=80,alias=''):
        virtualHostStr = __VIRTUALHOST__.format(serverPort,self.virtualHostDirectory,serverName,alias)
        self.writeToFile(self.configFilePath,virtualHostStr)


    # Add /etc/hosts (posix) server name
    def addHostName(self,serverName):
        hostsFilePath = __ETCHOSTS__[os.name.strip()]
        self.checkPathsExist(hostsFilePath)
        hostString = __HOSTNAME__.format('127.0.0.1',serverName)
        self.writeToFile(hostsFilePath,hostString)


    # Write given string to given file
    def writeToFile(self,fileDirectory,string):
        try:
            file = open(fileDirectory,'a')
            file.write(string)
            file.flush()
            file.close()
        except:
            print __ERRORS__['notopen'].format(fileDirectory)
            sys.exit(2)# Return with exit



