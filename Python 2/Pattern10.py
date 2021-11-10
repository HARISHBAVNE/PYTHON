# 5. Accept number of rows and number of columns from user and display
# below pattern.
# Input : iRow = 3 iCol = 4
# Output :  1 1 1 1
#           2 2 2 2
#           3 3 3 3
#           4 4 4 4

def Pattern(row,col):
    print()
    for i in range(1,row+1):
        for j in range (1,col+1):
            print(i,end = " ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()