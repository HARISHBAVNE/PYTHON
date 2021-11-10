from sys import *
import os,shutil
def FileCopy(src,dest):
    for Folder,Subfolder,File in os.walk(src):
        for file in File:
            print(file)
            shutil.copy((os.path.join(Folder,file)),(os.path.join(dest,file)))

def main():
    print("*****FIle Finder Application*******")
    print(f"Application script name is:{argv[0]}")

    if (len(argv)< 2):
        print("Insufficient Arguments")
        exit()
    if (argv[1]=='-u') or (argv[1]=='-U'):
        print("Usage:Use it as name.py")
        exit()
    if (argv[1]=='-h') or (argv[1]=='-H'):
        print("Help:This is file rename application")
        exit()
    FileCopy(argv[1],argv[2])
if __name__ == "__main__":
    main()
