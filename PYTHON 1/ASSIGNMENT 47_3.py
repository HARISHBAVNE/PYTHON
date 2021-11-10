# 3.Write a program which accept number from user and return the
# count of digits in between 3 and 7.
# Input : 2395    Input : 4521  Input : 9922
# Output : 1      Output : 2    Output : 0


#=============================================
# Function of Display Number between 3 and 7.
#=============================================
def CountRange(No):
    iDigit = 0
    iCnt = 0
    if (No<0):
        No = -No
    while(No>0):
        iDigit = No%10
        if ((iDigit > 3) and (iDigit < 7)):
            iCnt += 1
        No = No//10
    return iCnt
#==================
#Main Satrter.
#==================
def main():
    No = int(input("Enter a numbr"))
    Ret = CountRange(No)
    print(f"count of digits in between 3 and 7:{Ret}")
if __name__ == "__main__":
    main()
