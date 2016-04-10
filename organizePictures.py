import os.path
import time
import shutil
import filecmp
import ConfigParser

def create_directory(d):
    if not os.path.exists(d):
        os.makedirs(d)

def create_version_directory(currentFullFilePath):
    modifiedTime = os.path.getmtime(currentFullFilePath)
    createTime = os.path.getctime(currentFullFilePath)
    year = ""
    year_month = ""
    if modifiedTime < createTime:
        year = time.strftime('%Y', time.localtime(modifiedTime))
        year_month = time.strftime('%Y-%m', time.localtime(modifiedTime))        
    else:
        year = time.strftime('%Y', time.localtime(createTime))
        year_month = time.strftime('%Y-%m', time.localtime(createTime))
    return (year, year_month)

def file_exist_in_directory(directoryToCheck, fileToMove):
    for file in os.listdir(directoryToCheck):
        if not file.startswith("."):
            if filecmp.cmp(directoryToCheck + "/" + file, fileToMove):
                return True, 
    return False

def move_file(baseDirectory,currentFullFilePath,currentFileName,movedList,unmovedList):
    versionYear, versionFolder = create_version_directory(currentFullFilePath)
    versionDir = baseDirectory + "/" + versionYear + "/" + versionFolder
    newFile =  versionDir + "/" + currentFileName  
    
    create_directory(versionDir)

    if not file_exist_in_directory(versionDir, currentFullFilePath):
        print "Moving: " + currentFullFilePath + " To: " + newFile
        movedList.append(currentFullFilePath + "," + newFile)
        #shutil.copy(currentFullFilePath, versionDir)
        shutil.move(currentFullFilePath, newFile)
        return 1
    else:
        print "NOT Moving: " + currentFullFilePath + " To: " + newFile
        unmovedList.append(currentFullFilePath)
        return 0

def write_list_to_file(theList, theType):
    the_filename = "move_report/unmoved.txt"
    if theType == "moved":
        the_filename = "move_report/moved.txt"

    with open(the_filename, 'w+') as f:
        for s in theList:
            f.write(s + '\n')


def readConifg():
    config = ConfigParser.RawConfigParser()
    config.readfp(open('config.properties'))
    directory = config.get("Config", "directory") 
    videoDirectory = config.get("Config", "videoDirectory") 
    picturesDirectory = config.get("Config", "picturesDirectory") 
    return (directory, videoDirectory, picturesDirectory)

def main():
    directory, videoDirectory, picturesDirectory = readConifg()
    fileMoveCount = 0
    movedList = []
    unmovedList = []

    for dirpath, dirs, files in os.walk(directory):
        for currentFile in files:
            if not currentFile.startswith("."):
                # CURRENT file location full path
                currentFullFilePath = dirpath + "/" + currentFile
                #grab the file extension
                filename1, file_extension = os.path.splitext(currentFullFilePath) 
                #move the files
                if file_extension.lower() in (".mov", ".mp4"):
                    fileMoveCount += move_file(videoDirectory,currentFullFilePath,currentFile,movedList,unmovedList)
                else:
                    fileMoveCount += move_file(picturesDirectory,currentFullFilePath,currentFile,movedList,unmovedList)

    write_list_to_file(movedList, "moved")
    write_list_to_file(unmovedList, "unmoved")

    print "Total files moved: " + str(fileMoveCount)

main()
