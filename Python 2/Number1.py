#Write a program which accept number from user and display its multiplication of
#factors.
#Input : 12
#Output : 144 (1 * 2 * 3 * 4 * 6)

def MultFact(No):
    mult = 1
    for i in range(1,int(No/2)+1):
        if ((No%i) == 0):
            mult *= i
    return mult

def main():
    No = int(input("Enter a number:"))
    ret = MultFact(No)
    print(f"Multiplication of factor of Number {No} is:{ret}")
if __name__ == "__main__":
    main()
