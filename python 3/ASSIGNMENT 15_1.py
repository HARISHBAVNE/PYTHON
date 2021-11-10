# 1.Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.
from sys import *
import os
import hashlib

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
    
    if not os.path.exists(Directory):
        print("Invalid Directory")
        exit()
    for Folder,Subfolder,Files in os.walk(Directory):
        for file in Files:
            path = os.path.join(Folder,file)
            Hash = CalculateCheckSum(path)
            print()
            print(f"File name is:{file}")
            print(f"Cheecksum:{Hash}")
            print()
        

def main():
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
    
if __name__=="__main__":
    main()



