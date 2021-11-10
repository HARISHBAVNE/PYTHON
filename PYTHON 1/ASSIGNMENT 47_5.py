# 5.Write a program which accept number from user and return
# difference between summation of even digits and summation of odd digits.
# Input : 2395            Input : 1018            Input : 8440           Input : 5733
# Output : -15 (2 - 17)   Output : 6 (8 - 2)      Output : 16 (16 - 0)    Output : -18 (0 - 18)

#=============================================
# Function of Summation difference.
#=============================================
def CountDiff(No):
    iDigit = 0
    Even = 0
    Odd = 0
    if (No<0):
        No = -No
    while(No>0):
        iDigit = No%10
        if (iDigit%2 == 0):
            Even += iDigit
        elif (iDigit%2 != 0):
            Odd += iDigit
        No = No//10
    return ((Even)-(Odd))
#==================
#Main Satrter.
#==================
def main():
    No = int(input("Enter a numbr"))
    Ret = CountDiff(No)
    print(f"difference between summation of even digits and summation of odd digits:{Ret}")
if __name__ == "__main__":
    main()
