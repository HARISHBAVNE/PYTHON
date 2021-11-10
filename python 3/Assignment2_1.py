#Q1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
##for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.


#solution
#Import module 
from Arithmetic import *

def main():
    print("Enter first number")
    no1 = int(input())
    print("Enter Second number")
    no2 = int(input())
    
    ans1 = Add(no1,no2)
    ans2 = Sub(no1,no2)
    ans3 = Mult(no1,no2)
    ans4 = Div(no1,no2)

    print(f"Addition of {no1} and {no2} is: ",ans1)
    print(f"Substraction of {no1} and {no2} is: ",ans2)
    print(f"Multiplication of {no1} and {no2} is : ",ans3)
    print(f"Division of {no1} and {no2} is: ",ans4)
    

#Code Satrter
if __name__ == "__main__":
    main()
