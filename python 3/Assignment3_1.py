#Q1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130

#solution

import functools
def Addition(list):
    Add = functools.reduce(lambda no1,no2:no1+no2,list)
    return Add

def main():
    arr = []
    size= int(input("Enter number of elements"))
    
    for i in range(size):
        print(f"Enter no{i+1} element: ")
        value = int(input())
        arr.append(value)
    print(arr)

    ans = Addition(arr)
    print(ans)

# Code starter    
if __name__ == "__main__":
    main()
