__author__ = 'ugursogukpinar'

__TMPFOLDERS__ = {
    'posix'  : '/tmp/VHCreator/',
    'nt' : 'C:/tmp/VHCreator/'
}

__ERRORS__ = {
    'filenotfound' : 'There is no {folderName} folder in {directory}',
    'clonfail' : 'Clonning failed'
}
import subprocess,sys
class Git(object):

    def __init__(self,repoUrl,folderName,serverDirectory):
        # target folder to clone repository.
        self.folderName = folderName
        # Given directory. It should contain folderName
        self.directory = serverDirectory

        folderIndex = self.checkFolderName(self.folderName,self.directory)
        fullPath = self.createFullPath(folderIndex)
        self.execute('clone',repoUrl,fullPath)



    # Is there the folder name on path?
    def checkFolderName(self,folderName,serverDirectory):

        allFolders = serverDirectory.split('/')
        i = 0
        while((i < len(allFolders)) and (folderName != allFolders[i])):
            i += 1


        if(i == len(allFolders)):
            # Foldername not found.
            print __ERRORS__['filenotfound'].format(directory = serverDirectory,folderName = folderName)
            print __ERRORS__['clonfail']
            sys.exit(2)
        else:
            # Return folder index.
            return i+1


    # Create full path of found folder.
    def createFullPath(self,index):
        allFolders = self.directory.split('/')
        return '/'.join(allFolders[0:index])

    def execute(self,*args):
        try:
            subprocess.check_call(['git'] + list(args))
        except:
            print "Unexpected error: ",sys.exc_info()[0]
            sys.exit(2)


