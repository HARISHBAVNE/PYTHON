#3.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that
#numbers.
#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000


#solution
import functools

def main():
    arr = []
    size = int(input("Enter the no.of element: "))
    for i in range(size):
        value = int(input(f"Enter No{i+1} element: "))
        arr.append(value)
    print(arr)
    
    ans = list(filter(lambda no:(no >=70), arr))
    ans1= list(filter(lambda no: (no<=90),ans))
    print("Filtered number is: ",ans)
    ans2 = list(map(lambda no: (no + 10),ans1))
    print("Numbers after adding 10 is: ",ans2)
    ans3 = functools.reduce(lambda no1,no2: (no1 * no2),ans2)
    print("Multiplication of all number is: ",ans3)

# Code Starter
if __name__ == "__main__":
    main()
