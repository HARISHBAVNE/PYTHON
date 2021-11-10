#Q9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 Output : 7


#solution
def count(value):
    cnt = len(value)
    return cnt

def main():
    print("Enter a number")
    num = (input())
    ret = count(num)
    print(ret)

# Code Starter 
if __name__ == "__main__":
    main()
