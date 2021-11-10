# 5. Accept two file names from user which are existing files. Create one new file
# named as Demo.txt. Write name and Data of that three files in Demo.txt file one
# after another.
# Input : 
# pqr.txt
# xyz.txt

def CopyData(path1,path2,name):
    fd1 = open(path1,'r')
    fd2 = open(path2,'r')
    fd3 = open(name,'a')
    
    data = []
    data.append(fd1.read())
    data.append(fd2.read())
    fd3.write(path1)
    fd3.write(data[0])
    fd3.write(path1)
    fd3.write(data[1])
            


def main():
    path1 = input("Enter first file name:")
    path2 = input("Enter second file name:")
    path = input("Enter file name:")
   
    CopyData(path1,path2,path)
    

if __name__ == "__main__":
    main()
