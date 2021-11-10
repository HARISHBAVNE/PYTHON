# 3.Write a program which accept file name from user and create new file named as Demo.txt and
# copy all contents from existing file into new file. Accept file name through command line
# arguments.
# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt
import sys
class FileX:
    def __init__(self,name):
        self.name = name
    def FileD(self):
        with open(self.name,'r') as f1:
            with open("demo.txt",'a') as f2:
                for i in f1:
                    f2.write(i)
def main():
    FileName = sys.argv[1]
    obj = FileX(FileName)
    obj.FileD()
if __name__ == "__main__":
    main()
