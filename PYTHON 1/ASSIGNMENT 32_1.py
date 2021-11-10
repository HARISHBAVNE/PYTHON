# 1. Write application which accept two file names from user. Compare the contents of
# that two files. If contents are same then return true otherwise return false.
# Input : Demo.txt Hello.txt
# Output : Compare contents of Demo.txt and Hello.txt
class FileX:
    def __init__(self,Name1,Name2):
        self.FD1 = Name1
        self.FD2 = Name2
    

    def CompareFiles(self):
        fd1 = open(self.FD1,'r')
        fd2 = open(self.FD2,'r')
        data1 = []
        data1.append(fd1.read())
        data2 = []
        data2.append(fd2.read())
        if data1 == data2:
            return True
        else:
            return False
        
def main():
    FileName1 = input("Enter first file name:")
    FileName2 = input("Enter second file name:")
    
    obj = FileX(FileName1,FileName2)
    ret = obj.CompareFiles()
    print(ret)
if __name__ == "__main__":
    main()
