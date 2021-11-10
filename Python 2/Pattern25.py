# 5. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 4 iCol = 4
# Output : 1 2 3 4
#             2 3 4
#               3 4
#                 4


def Pattern(row, col):
    print()
    no = 1
    for i in range(1,row+1):
        for j in range(1,col+1):
            if (j>=i):
                print(i,end=" ")
                i += 1
            else:
                print(" ",end=" ")

        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))

    Pattern(row, col)


if __name__ == "__main__":
    main()
