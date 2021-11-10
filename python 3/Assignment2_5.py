#Q5.Write a program which accept one number for user and check whether number is prime or not.
#Input : 5 Output : It is Prime Numbernput : 12 Output : 16 (1+2+3+4+6)

#solution

def PrimeChk(value):
    for i in range(2,value):
        if (value%i == 0):
            return "Non Prime Number"
        else:
            return "Prime Number"
def main():
    num = int(input("Enter a number:"))
    ans = PrimeChk(num)
    print(f"{num}: is a",ans)
    
#Code starter
if __name__ == "__main__":
    main()
