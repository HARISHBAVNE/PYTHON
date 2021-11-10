#3. Write application which accept two file names from user. Append the contents of
#first file at the end of second file.
#Input : Demo.txt Hello.txt
#Output : Concat contents of Demo.txt at the end of Hello.txt

def concat(path1,path2):
    fd = open(path1,'r')
    fd2 = open(path2,'a')
    
    data = fd.read()
    for i in data:
        fd2.write(i)
def main():
    path1 = input("Enter first file name:")
    path2 = input("Enter second file name:")

    concat(path1,path2)
if __name__ == "__main__":
    main()
