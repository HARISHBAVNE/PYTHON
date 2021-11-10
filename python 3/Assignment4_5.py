#Q5.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
#return Maximum number from that numbers. (You can also use normal functions instead of #lambda functions).
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
#List after filter = [2, 11, 17, 23, 31]
#List after map = [4, 22, 34, 46, 62]
#Output of reduce = 62

#solution

import functools
#Normal function to find the prime number
def ChkPrime(arr):
    prime = []
    for i in (arr):
        chk = 0
        for j in range(2,i):
            if i%j == 0:
                chk = 1
                break
        if chk == 0:
            prime.append(i)
    return prime
    
def Mult(arr):
    multi = list(map(lambda no: (no*2),arr ))
    return multi
    
def main():
    arr = []
    size = int(input("Enter a number of element:"))
    for i in range(size):
        value = int(input(f"Enter a No{i+1} element: "))
        arr.append(value)
    print("Enter numbers are: ",arr)
    
    ans = ChkPrime(arr)
    print("Prime numbers are: ",ans)

    ans1 = Mult(ans)
    print("Numbers after multiplied by 2 :",ans1)

    ans1.sort()                              # Maximum number using sort method  
    print("Maximum number using sort method is: ",ans1[-1])

    ans2 =max(ans1)                         #Maximum number using max function
    print("Maximum number using max function:",ans2)
# Code Starter
if __name__ == "__main__":
    main()
