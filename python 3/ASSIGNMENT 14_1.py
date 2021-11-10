from sys import *
import os

def FileFinder(Directory,ext):
    for Folder,Subfolder,File in os.walk(Directory):
        print(f"Folder name is:{Folder}")
        for sub in Subfolder:
            print(f"Sub folder from Folder is:{Subfolder}")
        for file in File:
            if (file.endswith(ext)):
                print(file)
            

def main():
    print("*****FIle Finder Application*******")
    print(f"Application script name is:{argv[0]}")

    # if (len(argv)= 2):
        # print("Insufficient Arguments")
        # exit()
    if (argv[1]=='-u') or (argv[1]=='-U'):
        print("Usage:Use it as name.py")
        exit()
    if (argv[1]=='-h') or (argv[1]=='-H'):
        print("Help:This application is use as a file finder")
        exit()
    FileFinder(argv[1],argv[2])
if __name__ == "__main__":
    main()
