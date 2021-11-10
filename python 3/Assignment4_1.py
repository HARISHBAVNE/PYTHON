#1.Write a program which contains one lambda function which accepts one parameter and return
#power of two.
#Input : 4 Output : 16
#SInput : 6 Output : 36

#solution
def Power(no):
    p = (lambda no: no**2)
    ret = p(no)
    return ret

def main():
    num = int(input("Enter a number: "))
    ans = Power(num)
    print(f"Power of two of No.{ans} is:")
if __name__ == "__main__":
    main()
