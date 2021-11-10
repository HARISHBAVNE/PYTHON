def matrix(row,col):
    m = []
    for i in range(row):
        l = []
        for j in range(col):
            l.append(int(input()))
        m.append(l)
    return m
    
def main():
    row = int(input("Enter a number of row:"))
    col = int(input("Enter a number of column:"))

    ret = matrix(row,col)
    for i in range(row):
        for j in range(col):
            print(ret[i][j],end = " ")
        print()
if __name__ == "__main__":
    main()
