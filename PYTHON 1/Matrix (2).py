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
    HourGlass = []
    for i in range(row):
        for j in range(col):
            if ((j==0)or(j==col-1)or(i==0)or(i==row-1)):
                continue
            else:  
                Sum = (ret[i][j])+(ret[i-1][j-1])+(ret[i-1][j])+(ret[i-1][j+1])+(ret[i+1][j-1])+(ret[i+1][j])+(ret[i+1][j+1])
                HourGlass.append(Sum)
    print(max(HourGlass))
if __name__ == "__main__":
    main()
