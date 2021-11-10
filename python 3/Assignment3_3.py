#Q3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5


#solution

#Minimum number function using loop
def MinimumN(list):
    Min = list[0]
    for i in range(len(list)):
        if list[i] < Min:
            Min = list[i]
    return Min

#Using Min function
def Min(list):
    return min(list)

def main():
    arr = []
    size = (int(input("Enter the number of Elements: ")))
    
    for i in range(size):
        value = int(input(f"Enter no{i+1} element:"))
        arr.append(value)
    print("Entered list is: ",arr)
    
    ans1 = MinimumN(arr)
    print("Minimum number using loop is: ",ans1)
    
    ans2 = Min(arr)
    print("Minimum number using Min function is: ",ans2)

# Code starter    
if __name__ == "__main__":
    main()
