# 2.Write a program which accept number from user and return the count of odd digits.
# Input : 2395     Input : 1018
# Output : 3       Output : 2

# Input : 8462    Input : -1018
# Output : 0      Output : 2

#========================
# Function of Odd count.
#========================
def CountOdd(No):
    iDigit = 0
    iCnt = 0
    if (No<0):
        No = -No
    while(No>0):
        iDigit = No%10
        if ((iDigit%2)!=0):
            iCnt += 1
        No = No//10
    return iCnt
#==================
#Main Satrter.
#==================
def main():
    No = int(input("Enter a numbr"))
    Ret = CountOdd(No)
    print(f"Count of Odd digit in Number is:{Ret}")

if __name__ == "__main__":
    main()
