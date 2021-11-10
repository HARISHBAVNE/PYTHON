#10. Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934 Output : 37


#solution

def AddDigits(value):
    sum = 0
    for i in range(len(str(value))):
        digits = value%10
        sum = sum + digits
        value = value//10
    return sum
    
def main():
    print("Enter a number")
    num = int(input())
    ret = AddDigits(num)
    print(ret)

# Code Starter 
if __name__ == "__main__":
    main()
