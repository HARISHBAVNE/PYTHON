# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”
# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.
# After execution this script each .txt file gets renamed as .doc.

from sys import *
import os
from pathlib import Path

def FileFinder(Directory,ext1,ext2):
    for Folder,Subfolder,File in os.walk(Directory):
        print(f"Folder name is:{Folder}")
        for sub in Subfolder:
            print(f"Sub folder from Folder is:{Subfolder}")
        for file in File:
            if file.endswith(ext1):
                path = os.path.join(Folder)
                print(file)
                
                
                

def main():
    print("*****FIle Finder Application*******")
    print(f"Application script name is:{argv[0]}")

    # if (len(argv)< 2):
        # print("Insufficient Arguments")
        # exit()
    if (argv[1]=='-u') or (argv[1]=='-U'):
        print("Usage:Use it as name.py")
        exit()
    if (argv[1]=='-h') or (argv[1]=='-H'):
        print("Help:This is file rename application")
        exit()
    FileFinder(argv[1],argv[2],argv[3])
if __name__ == "__main__":
    main()
