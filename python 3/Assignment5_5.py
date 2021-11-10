# Q5. Write a recursive program which accept number from user and return its
# factorial.
# Input : 5
# Output : 120

#solution

def Fact(value):
    if (value==0):
        return 1
    else:
        return ((value)*Fact(value-1))

def main():
    No = int(input("Enter a number:"))
    ret = Fact(No)
    print(f"Factorial of {No} is: ",ret)

#Code starter
if __name__ == "__main__":
    main()
