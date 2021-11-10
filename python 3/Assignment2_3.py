#Q3. Write a program which accept one number from user and return its factorial.
#Input : 5 Output : 120


#solution

def Fac(value):
    fact = 1
    for i in range(1,value+1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter a number to generate factorail number: "))
    ret = Fac(num)
    print(f"factorial of {num} is = ",ret)
        

#Code starter
if __name__ == "__main__":
    main()
