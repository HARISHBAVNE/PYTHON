# 3. Accept number of rows and number of columns from user and display
# below pattern.
# Input : iRow = 3 iCol = 5
# Output : 5 4 3 2 1
         # 5 4 3 2 1
         # 5 4 3 2 1

def Pattern(row,col):
    for i in range(row):
        for j in range (col,0,-1):
            print(j,end = " ")
        print()


def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of columns:"))
    
    Pattern(row,col)

if __name__ == "__main__":
    main()