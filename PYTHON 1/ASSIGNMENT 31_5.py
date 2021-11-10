# 5. Write application which accept file name from user and one string from user. Write
# that string at the end of file.
# Input : Demo.txt
# Hello World
# Output : Write Hello World at the end of Demo.txt file
class FileX:
    def __init__(self,Name,Data):
        self.FD = Name
        self.Data = Data

    def WriteData(self):
        fd = open(self.FD,'a')
        fd.write(self.Data)
        fd.close()
        
def main():
    FileNmae = input("Enter file name:")
    Data = input("Write data to add in file at end of File:")
    
    obj = FileX(FileNmae,Data)
    obj.WriteData()


if __name__ == "__main__":
    main()
