#Q2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.
#Input : 4 3 Output : 12
#Input : 6 3 Output : 18


#solution
def Mult(no1,no2):
    M = lambda no1,no2: no1*no2
    ret = M(no1,no2)
    return ret
def main():
    num1 = int(input("Enter a first Number:"))
    num2 = int(input("Enter a second Number:"))
    
    ans = Mult(num1,num2)
    print(f"Multiplication of {num1} & {num2} is:",ans)
if __name__ == "__main__":
    main()
