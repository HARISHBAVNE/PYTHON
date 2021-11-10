# 1. Write a recursive program which accept number from user and display below
# pattern.
# Input : 5
# Output : 5 * 4 * 3 * 2 * 1 *

def fun(no):
    while(no>0):
        print(f"{no}*",end=" ")
        no -= 1
    print()

def fun1(no):
    if (no>0):
        print(f"{no}*",end =" ")
        fun(no-1)

def main():
    number = int(input("Enter a number:"))
    fun(number)
    fun1(number)
if __name__ == "__main__":
    main()
