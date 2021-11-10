#Q4.Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3

#solution

def Frequency(list):
    no = (int(input("Enter a element to search: ")))
    return list.count(no)

def main():
    arr = []
    size = (int(input("Enter the number of Elements: ")))
    
    for i in range(size):
        value = int(input(f"Enter no{i+1} element:"))
        arr.append(value)
    print("Entered list is: ",arr)

    ans = Frequency(arr)
    print(ans)

# Code starter    
if __name__ == "__main__":
    main()
