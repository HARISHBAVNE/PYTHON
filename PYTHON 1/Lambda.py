# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

import functools

def fun(l):
    
    l1 = list(filter(lambda no:no>=70 and no<=90,l))            #filter function using lambda function
    print("filtered elements:",l1)                              # Gives filtered output(elements which is No >= 70 and No <= 90)

    l2 = list(map(lambda no:no+10,l1))                          #Map function using lambda function
    print("Mapped object:",l2)                                  # Gives mapped output(adding 10 into each element)                    
                                                            
    if len(l2) == 0:
        print("There is no elements in list for reduce function")
    else:
        l3 = functools.reduce(lambda no1,no2:no1*no2 , l2)      #Reduce function using lambda function
        print("multiplication of all numbers:",l3)              #Gives reduced output(multiplication of each element)


def main():
    l = []                                                      #Dynamic list
    print("Enter size of list")
    size = int(input())
    print(f"Enter {size} elements")
    for i in range(size):
        print(f"Enter {i+1}th element:")
        value = int(input())
        l.append(value)
    print("Entered list:",l)

    fun(l)                                                      #Calling to function
    
if __name__ == "__main__":
    main()
