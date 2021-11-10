# 5. Accept N numbers from user and display summation of digits of each
# number.
# Input : N : 6
# Elements : 8225 665 3 76 953 858
# Output : 17 17 3 13 17 21

def Display(Arr,size):
    for i in range(size):
        iSum = 0
        No = Arr[i]
        while(No > 0):
            if ((No%10)!=0):
                iSum = iSum +(No%10)
            No = No//10
        print(iSum,end = " ")

def main():
    iSize = int(input("Enter number of elements"))
    Arr = []
    print("Enter the elements")
    for i in range(iSize):
        Value = int(input(f"Enter element {i+1}:"))
        Arr.append(Value)
    Display(Arr,iSize)
if __name__ == "__main__":
    main()
        
        