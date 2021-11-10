#Q4.Write a recursive program which accept number from user and return
#summation of its digits.
#Input : 879
#Output : 24

#solution

def Sum(value):
    if (value==0):
        return 0
    else:
        return ((value%10)+Sum(value//10))

def main():
    No = int(input("Enter a number"))
    ret = Sum(No)
    print("Summation is: ",ret)

#Code starter
if __name__ == "__main__":
    main()
