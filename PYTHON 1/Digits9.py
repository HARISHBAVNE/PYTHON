# 4.Write a program which accept number from user and return multiplication of all
# digits.
# Input : 2395
# Output : 270
# Input : 1018
# Output : 8
# Input : 9440
# Output : 144
def Mult(No):
    mult = 1
    Digit = 0
    if (No < 0):
        No = -(No)
    while(No > 0):
        Digit = (No%10)
        if (Digit != 0):
            mult = mult * Digit 
        No = No//10
    return mult

def main():
    No = int(input("Enter a number:"))
    ret = Mult(No)
    print(f"Digit multiplication is:{ret}")

if __name__ == "__main__":
    main()
