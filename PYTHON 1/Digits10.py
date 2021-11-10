# 5.Write a program which accept number from user and return difference between
# summation of even digits and summation of odd digits.
# Input : 2395
# Output : -15 (2 - 17)
# Input : 1018
# Output : 6 (8 - 2)
# Input : 8440
# Output : 16 (16 - 0)
def Diff(No):
    sum1 = 0
    sum2 = 0
    if (No < 0):
        No = -(No)
    while(No > 0):
        Digit = (No%10)
        if ((Digit%2)==0):
            sum1 = sum1 + Digit
        else:
            sum2 = sum2 + Digit
        No = No//10
    return (sum1 - sum2)

def main():
    No = int(input("Enter a number:"))
    ret = Diff(No)
    print(f"Differnece betwwen sum of even and odd digits is:{ret}")

if __name__ == "__main__":
    main()
