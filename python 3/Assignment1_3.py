#Q3. Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.
#Input : 11 5 Output : 16

#Solution:

# Function for Addition of Two numbers
def Add(value1,value2):
    addition = value1 + value2
    return (addition)

def main():
    print("Enter two numbers to perform addition")
    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter Second Number: "))
    ans = Add(num1,num2)
    print(f"Additon of {num1} and {num2} is: ",ans) # Sting formating

# code starter    
if __name__ == "__main__":
    main()
