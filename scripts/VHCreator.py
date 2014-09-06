__author__ = 'ugursogukpinar'

import os,sys

__ERRORS__ = {
    'notfound' : '{} file not found.',
    'notopen' : '{} can\'t open. Try with root priviliges.'
}

__VIRTUALHOST__ = '''
    # Added with VHCreator
    # Alias of VirtualHost \'{3}\'
    <VirtualHost *:{0}>
        DocumentRoot : {1}
        ServerName : {2}
    </VirtualHost>
'''

__ETCHOSTS__ = {
    'posix' : '/etc/hosts',
    'nt' : 'C:\Windows\System32\Drivers\etc\hosts'
}

__HOSTNAME__ = '{0}         {1}'

class VHCreator(object):
    def __init__(self,configFilePath,virtualHostDirectory):
        self.configFilePath = configFilePath
        self.virtualHostDirectory = virtualHostDirectory
        self.checkPathsExist(self.configFilePath)
        # self.checkPathsExist(self.virtualHostDirectory)

    # Check configuration file exist
    def checkPathsExist(self,filePath):
        if(os.path.isfile(filePath) == False):
            print __ERRORS__['notfound'].format(filePath)
            sys.exit(1) #  Return with exit


    def addVirtualHost(self,serverName,serverPort=80,alias=''):
        virtualHostStr = __VIRTUALHOST__.format(serverPort,self.virtualHostDirectory,serverName)
        self.writeToFile(self.configFilePath,virtualHostStr)

    def addHostName(self,serverName):
        hostsFilePath = __ETCHOSTS__[os.name.strip()]
        self.checkPathsExist(hostsFilePath)
        hostString = __HOSTNAME__.format('127.0.0.1',serverName)
        self.writeToFile(hostsFilePath,hostString)


    def writeToFile(self,fileDirectory,string):
        try:
            file = open(fileDirectory,'a')
            file.write(string)
            file.flush()
            file.close()
        except:
            print __ERRORS__['notopen'].format(fileDirectory)
            sys.exit(1) # Return with exit



