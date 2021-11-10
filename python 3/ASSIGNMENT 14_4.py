from sys import *
import os,shutil
def FileCopy(src,dest,ext):
    dir = dest
    currentD = os.getcwd()
    path = os.path.join(currentD,dir)
    os.mkdir(path)
    for Folder,Subfolder,File in os.walk(src):
        for file in File:
            if file.endswith(ext):
                path = os.path.join(Folder,file)
                shutil.copy((os.path.join(Folder,file)),(dir))

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
    FileCopy(argv[1],argv[2],argv[3])
if __name__ == "__main__":
    main()
