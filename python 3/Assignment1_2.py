#Q2. Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.
#Input : 11 Output : Odd Number
#Input : 8 Output : Even Number


#Solution:
def ChkNum(Value):
    if Value%2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    print("Enter a Number for checking whether it is Even or Odd")
    Num = int(input())
    Ans = ChkNum(Num)
    print(f"{Num} is: ",Ans)

# Code starter
if __name__ == "__main__":
    main()
