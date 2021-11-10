# 4.Write a program which accept number from user and return
# multiplication of all digits.
# Input : 2395     Input : 1018   Input : 9440    Input : 922432
# Output : 270     Output : 8     Output : 144    Output : 864



#=============================================
# Function of Multiplication of all digits.
#=============================================
def Multiply(No):
    iDigit = 0
    iMult = 1
    if (No<0):
        No = -No
    while(No>0):
        iDigit = No%10
        if (iDigit!=0):
            iMult = iMult * iDigit 
        No = No//10
    return iMult
#==================
#Main Satrter.
#==================
def main():
    No = int(input("Enter a numbr"))
    Ret = Multiply(No)
    print(f"Product of all digits is:{Ret}")
if __name__ == "__main__":
    main()
