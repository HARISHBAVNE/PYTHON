# 5. Accept three file names from user which are existing files. Create one new file
# named as Demo.txt. Write name and Data of that three files in Demo.txt file one
# after another.
# Input : abc.txt
# pqr.txt
# xyz.txt
# Output : Write file name and data of each file in Demo.txt file.
class FileX:
    def __init__(self,name1,name2,name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    def WordCounter(self):
        with open("demo.txt",'a') as WF:
            fd = [self.name1,self.name2,self.name3]
            for i in range(len(fd)):
                with open(fd[i],'r') as RF:
                    for j in RF:
                        WF.write(fd[i])
                        WF.write(j)
        
def main():
    name1 = input("Enter first file name:")
    name2 = input("Enter second file name:")
    name3 = input("Enter third file name:")
    obj = FileX(name1,name2,name3)
    obj.WordCounter()

if __name__ == "__main__":
    main()
