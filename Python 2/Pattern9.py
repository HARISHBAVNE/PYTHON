# 4. Accept number of rows and number of columns from user and display
# below pattern.
# Input : iRow = 3 iCol = 4
# Output :  * # * #
#           * # * #
#           * # * #

def Pattern(row,col):
    print()
    for i in range(row):
        for j in range (1,col+1):
            if (j%2 != 0):
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