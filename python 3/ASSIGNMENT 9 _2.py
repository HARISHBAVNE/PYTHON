# 2. Write a program which accept file name from user and open that file and display the contents
# of that file on screen.
# Input : Demo.txt
# Display contents of Demo.txt on console.

class FileX:
    def __init__(self,FName):
        self.FName = FName
    def FileReader(self):
        with open(self.FName,'r') as FD:
            print(FD.read())

def main():
    FileName = input("Enter file name:")
    obj = FileX(FileName)
    obj.FileReader()
   
if __name__ == "__main__":
    main()
