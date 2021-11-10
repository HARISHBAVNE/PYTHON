# 4. Write application which accept file name and one word from user. Count the
# frequency of that word in file.
# Input : Marvellous.txt
# Hello
# Output : Count the frequency if Hello in Marvellous.txt file.

class FileX:
    def __init__(self,name,word):
        self.name = name
        self.word = word
    def WordCounter(self):
        fd = open(self.name,'r')
        Data = (fd.read()).split()
        count = 0
        for i in range(len(Data)):
            if Data[i] == self.word:
                count += 1
        return count

def main():
    FileName = input("Enter file name:")
    Word = input("Enter word to count its frequency from file data:")
    obj = FileX(FileName,Word)
    ret = obj.WordCounter()
    print("Frequency of word is:",ret)

if __name__ == "__main__":
    main()
