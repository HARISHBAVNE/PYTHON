# 5. Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Marvellous
# Search “Marvellous” in Demo.txt

class FileX:
    def __init__(self):
        self.FileName = 0
        self.Data = 0
    def Accept(self):
        self.FileName = input("Enter the file name:")
        self.Data = input("Enter word to calculate frequency:")
    def WordCounter(self):
        with open(self.FileName,'r') as F:
            FData = (F.read()).split()
            count = 0
            for i in range(len(FData)):
                if self.Data == FData[i]:
                    count = count + 1
            return count               


def main():
    obj = FileX()
    obj.Accept()
    ret = obj.WordCounter()
    print("Frequency is:",ret)
    
if __name__ == "__main__":
    main()
