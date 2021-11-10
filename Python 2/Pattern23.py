# 3. Accept number of rows and number of columns from user and display below
# pattern.
# Input : iRow = 5 iCol = 5
# Output :  $ * * * *
#           # $ * * *
#           # # $ * *
#           # # # $ *
#           # # # # $


def Pattern(row, col):
    print()
    no = 1
    for i in range(1,row+1):
        for j in range(1,col+1):
            if (i<j):
                print("*", end=" ")
            elif(i==j):
                print("$",end=" ")
            else:
                print("#",end=" ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))

    Pattern(row, col)


if __name__ == "__main__":
    main()
