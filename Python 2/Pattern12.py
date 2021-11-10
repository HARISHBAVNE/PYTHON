# 2. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 4 iCol = 4
# Output : A B C D
#          a b c d
#          A B C D
#          a b c d

def Pattern(row,col):
    print()
    ch = ord("A")
    for i in range(row):
        for j in range (col):
            if ((i%2)==0):
                print(chr(ch+j),end = " ")
            else:
                print(chr((ch+j)+32),end = " ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()