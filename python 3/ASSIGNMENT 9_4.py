# 4.Write a program which accept two file names from user and compare contents of both the
# files. If both the files contains same contents then display success otherwise display failure.
# Accept names of both the files from command line.
# Input : Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt
import sys
class FileX:
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def FileD(self):
        with open(self.name1,'r') as f1:
            with open(self.name2,'r') as f2:
                F1Data = f1.readlines()
                F2Data = f2.readlines()
                if F1Data == F2Data:
                    return True
                else:
                    return False
                            
def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]
    obj = FileX(FileName1,FileName2)
    ret = obj.FileD()
    if ret == True:
        print("Success")
    else:
        print("Failure")
        
if __name__ == "__main__":
    main()
