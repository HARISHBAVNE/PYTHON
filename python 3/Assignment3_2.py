#Q2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56


#solution

#Maximum number function using loop
def MaximumN(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

#Using Max function
def Maximum(list):
    return max(list)

def main():
    arr = []
    size = (int(input("Enter the number of Elements: ")))
    
    for i in range(size):
        value = int(input(f"Enter no{i+1} element:"))
        arr.append(value)
    print("Entered list is: ",arr)
    
    ans1 = MaximumN(arr)
    print("Maximum number using loop is: ",ans1)
    
    ans2 = Maximum(arr)
    print("Maximum number using Max function is: ",ans2)

# Code starter    
if __name__ == "__main__":
    main()
