#1.Write a program which accept number from user and return the
#count of even digits.
#Input : 2395
#Output : 1
#Input : 1018
#Output : 2
#Input : -1018
#Output : 2
#========================
# Function of Even count.
#========================
def CountEven(No):
    iDigit = 0
    iCnt = 0
    if (No<0):
        No = -No
    while(No>0):
        iDigit = No%10
        if ((iDigit%2)==0):
            iCnt += 1
        No = No//10
    return iCnt
#==================
#Main Satrter.
#==================
def main():
    No = int(input("Enter a numbr"))
    Ret = CountEven(No)
    print(f"Count of Even digit in Number is:{Ret}")

if __name__ == "__main__":
    main()
