# 4.Write a program which accept number from user and return summation of all its
# non factors.
# Input : 12
# Output : 50

def SumNonFact(No):
    Sum = 0
    for i in range(1,No):
        if ((No%i) != 0):
            Sum += i
    
    return Sum
    

def main():
    No = int(input("Enter a number:"))
    ret = SumNonFact(No)
    print(f"Sumation of Non Factors of {No} is:{ret}")
if __name__ == "__main__":
    main()
