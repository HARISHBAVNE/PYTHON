# 1. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 4 iCol = 4
# Output : * # # #
#          * * # #
#          * * * #
#          * * * *

def Pattern(row,col):
    print()
    no = 1
    for i in range(row):
        for j in range (col):
            if (j <= i):
                print("*",end = " ")
            else:
                print("#",end = " ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()