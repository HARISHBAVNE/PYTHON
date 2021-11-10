# 4. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 6 iCol = 6
# Output : * * * * *  * *
#          *  *         *
#          *    *       *
#          *       *    *
#          *         *  *
#          * * * * * *  *


def Pattern(row, col):
    print()
    no = 1
    for i in range(1,row+1):
        for j in range(1,col+1):
            if ((i==1)or(i==row)or(j==1)or(j==col)or(j==i)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))

    Pattern(row, col)


if __name__ == "__main__":
    main()
