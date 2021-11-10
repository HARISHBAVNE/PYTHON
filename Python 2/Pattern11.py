# 1. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 4 iCol = 4
# Output : A B C D
#          A B C D
#          A B C D
#          A B C D

def Pattern(row,col):
    print()
    ch = ord("A")
    for i in range(1,row+1):
        for j in range (col):
            print(chr(ch+j),end = " ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()