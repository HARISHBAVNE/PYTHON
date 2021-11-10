# pattern.
# Input : iRow = 4 iCol = 4
# Output : 1 2  3  4  5
#          1  2       5
#          1    3     5
#          1       4  5
#          1  2 3  4  5

def Pattern(row, col):
    print()
    no = 1
    for i in range(1,row+1):
        for j in range(1,col+1):
            if (i==j)or(i==1)or(i==row)or(j==1)or(j==col):
                print(j,end=" ")
            else:
                print(" ",end=" ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))

    Pattern(row, col)


if __name__ == "__main__":
    main()
