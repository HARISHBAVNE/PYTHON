# 2. Accept number of rows and number of columns from user and display
# below pattern.
# Input : iRow = 4 iCol = 3
# Output :  1 2 3
#           1 2 3
#           1 2 3
#           1 2 3

def Pattern(row,col):
    for i in range(row):
        for j in range (1,col+1):
            print(j,end = " ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()