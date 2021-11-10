# 2. Write application which accept file name and one character from user. Count the
# frequency of that character in file.
# Input : Demo.txt
# M
# Output : Count occurrence of M in Demo.txt

def countletter(path,ch):
    fd = open(path,'r')
    icnt = 0
    data = fd.read()
    for i in data:
        if (i == ch):
            icnt += 1
    return icnt

def main():
    path = input("Enter file name:")
    ch = input("Enter a character to count the frequency:")
    ret = countletter(path,ch)
    print(f"Frequecny of character {ch} is:{ret}")

if __name__ == "__main__":
    main()