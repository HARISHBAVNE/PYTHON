# 5.Write a program which accept number from user and return difference between
# summation of all its factors and non factors.
# Input : 12
# Output : -34 (16 - 50)

def DiffFact(No):
    SumF = 0
    SumNF = 0
    for i in range(1,int(No/2)+1):
        if ((No%i) == 0):
            SumF += i
    
    for i in range(1,No):
        if ((No%i) != 0):
            SumNF += i
    
    return (SumF - SumNF)
    

def main():
    No = int(input("Enter a number:"))
    ret = DiffFact(No)
    print(f"Difference of summation of Factors of {No} is:{ret}")
if __name__ == "__main__":
    main()
