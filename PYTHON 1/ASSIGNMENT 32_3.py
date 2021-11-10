# 3. Write application which accept two file names from user. Append the contents of
# first file at the end of second file.
# Input : Demo.txt Hello.txt
# Output : Concat contents of Demo.txt at the end of Hello.txt
class FileX:
    def __init__(self,Name1,Name2):
        self.FD1 = Name1
        self.FD2 = Name2

    def WriteData(self):
        fd1 = open(self.FD1,'r')
        fd2 = open(self.FD2,'a')
        for i in fd1:
            fd2.write(i)
        
        
def main():
    FileNmae1 = input("Enter first file name:")
    FileNmae2 = input("Enter Second file name:")
    
    
    obj = FileX(FileNmae1,FileNmae2)
    obj.WriteData()


if __name__ == "__main__":
    main()
