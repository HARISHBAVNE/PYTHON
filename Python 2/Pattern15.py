# 5. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 3 iCol = 4
# Output : 1 2 3 4
#          5 6 7 8
#          9 10 11 12

def Pattern(row,col):
    print()
    no = 1
    for i in range(row):
        for j in range (col):
            print(no,end = " ")
            no = no + 1
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()