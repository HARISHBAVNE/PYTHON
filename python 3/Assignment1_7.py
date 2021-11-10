#Q7. Write a program which contains one function that accept one number from user and returns
#true if number is divisible by 5 otherwise return false.
#Input : 8 Output : False
#Input : 25 Output : True


#Solution:
def TF(value):
    if value%5 == 0:
        return True
    else:
        return False
def main():
    print("Enter a number for checking is it divisivle by 5 or not")
    no = int(input())
    ans = TF(no)
    print("{} is divisble by 5 is True or False: ".format(no),ans) # String formating using format method

# Code starter
if __name__ == "__main__":
    main()
