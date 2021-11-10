# 3. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 3 iCol = 5
# Output : A A A A A
#          B B B B B
#          C C C C C

def Pattern(row,col):
    print()
    ch = ord("A")
    for i in range(row):
        for j in range (col):
            print(chr(ch),end = " ")
        ch = ch+1
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()