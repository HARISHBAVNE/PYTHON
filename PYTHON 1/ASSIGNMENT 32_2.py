# 2. Write application which accept file name and one character from user. Count the
# frequency of that character in file.
# Input : Demo.txt
# M
# Output : Count occurrence of M in Demo.txt
class File:
    def __init__(self,name,char):
        self.name = name
        self.char = char
    def Filex(self):
        fd = open(self.name,'r')
        lines = fd.readlines()
        count = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if ((lines[i])[j]) == self.char:
                    count = count + 1
        return count
    
        fd.close()
    
def main():
    name = input("Enter file path:")
    char = input("Enter character to find frequency of that character from file data:")
    obj = File(name,char)
    ret = obj.Filex()
    print(f"Count occurrence of char from file is:{ret}")
if __name__ == "__main__":
    main()
