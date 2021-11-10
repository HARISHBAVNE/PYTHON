# 2. Accept N numbers from user and return the smallest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 3

def Smallest(Arr,iSize):
    mini = Arr[0]
    for i in range(iSize):
        if (Arr[i]<mini):
            mini = Arr[i]
    return mini
def main():
    print("Enter Number of elements")
    iSize = int(input())
    Arr = []
    print("Enter elements")
    for i in range(iSize):
        Value = int(input("Enter element {}: ".format(i+1)))
        Arr.append(Value)
    print("Entered elements in sequence:",Arr)
    
    iRet = Smallest(Arr,iSize)
    print(f"Smallest number from sequence is:{iRet}")
if __name__ == "__main__":
    main()