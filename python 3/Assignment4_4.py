#4.Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204


#solution
import functools

def main():
    arr = []
    size = int(input("Enter the no.of element: "))
    for i in range(size):
        value = int(input(f"Enter No{i+1} element: "))
        arr.append(value)
    print(arr)
    
    ans = list(filter(lambda no: (no%2==0),arr))
    print("Even numbers are: ",ans)
    ans1 = list(map(lambda no:(no**2),ans))
    print("Squar of numbers: ",ans1)
    ans2 = functools.reduce(lambda no1,no2:(no1+no2),ans1)
    print("Addition of all number is: ",ans2)

# Code Starter
if __name__ == "__main__":
    main()
