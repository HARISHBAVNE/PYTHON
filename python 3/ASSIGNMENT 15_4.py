# 4. Design automation script which accept directory name and delete all duplicate files from that
# directory. Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory. Display execution time required for the
# script.
# Usage : DirectoryDusplicateRemoval.py “Demo”
# Demo is name of directory.
Piyush
from sys import *
import os
import hashlib
import time

def CalculateCheckSum(path,blocksize = 1024):
    fd = open(path,'rb')
    hobj = hashlib.md5()
    
    buffer = fd.read(blocksize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fd.read(blocksize)
    
    return hobj.hexdigest() 
    fd.close()
def FileCheckSum(Directory):
    Duplicate = {}
    LogPath = os.path.join(os.getcwd(),"log.txt")
    fd = open(LogPath,'a')
    if not os.path.exists(Directory):
        print("Invalid Directory")
        exit()
    
    for Folder,Subfolder,Files in os.walk(Directory):
        for file in Files:
            path = os.path.join(Folder,file)
            Hash = CalculateCheckSum(path)
            if Hash in Duplicate:
                Duplicate[Hash].append(file)
                fd.write(f"{file}\n")
                os.remove(path)
                
            else:
                Duplicate[Hash] = [file]
    return (Duplicate)


def main():
    start = time.time()
    print(f"Application file is:{argv[0]}")
    
    if (len(argv)<2):
        print("Insufficient arguments")
        exit()
    if (argv[1]=="- u") or (argv[1]=="-U"):
        print("Usage: This application is use to find the checksum of files.")
        exit()

    if (argv[1]=="- h") or (argv[1]=="-H"):
        print("Help: Provide directory")
        exit()
    
    FileCheckSum(argv[1])

    print(ret)
    end = time.time()
    print("execution time required for the Application is:",end-start)
if __name__=="__main__":
    main()



