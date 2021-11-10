#5.Write a program which accept N numbers from user and store it into List. Return addition of all
#prime numbers from that List. Main python file accepts N numbers from user and pass each
#number to ChkPrime() function which is part of our user defined module named as
#MarvellousNum. Name of the function from main python file should be ListPrime().
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 10 34 2 5 8
#Output : 32 (13 + 5 + 7 +2 + 5)

#solution
import functools
def ChkPrime(arr):
    prime = []
    for i in (arr):
        fact=0
        for j in range(2,i):
            if i%j == 0:
                fact=1
                break
        if fact==0:
            prime.append(i)
    print(prime)

    Add = functools.reduce(lambda no1,no2: no1 + no2 , (prime))
    return Add
    
