# 1.Write a program which accepts file name from user and check whether that file exists in
# current directory or not.
# Input : Demo.txt
# Check whether Demo.txt exists or not.

class FileX:
    def __init__(self,FName):
        self.FName = FName
    def FileFinder(self):
        try:
            with open(self.FName,'r') as F:
                return True
        except:
            return False

def main():
    FileName = input("Enter file name:")
    obj = FileX(FileName)
    ret = obj.FileFinder()
    if ret == True:
        print("File exists")
    else:
        print("File not exists")
if __name__ == "__main__":
    main()
