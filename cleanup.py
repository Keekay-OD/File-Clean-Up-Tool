import glob
import os



def scandirs(path):
    for root, dirs, files in os.walk(path):
        for currentFile in files:
            print ("processing file: " + currentFile)
            exts = ('.jpg', '.png')
            if currentFile.lower().endswith(exts):
                os.remove(os.path.join(root, currentFile))


scandirs('/Users/omardiaz/Desktop/Coding Projects/File Clean Up Tool/samples')