# 3. Accept N numbers from user and return the difference between largest
# and smallest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 90 (93 -3)

def Diff(Arr,iSize):
    mini = Arr[0]
    maxi = Arr[0]
    for i in range(iSize):
        if (Arr[i]<mini):
            mini = Arr[i]
        elif (Arr[i]>maxi):
            maxi = Arr[i]
    return (maxi-mini)
    
def main():
    print("Enter Number of elements")
    iSize = int(input())
    Arr = []
    print("Enter elements")
    for i in range(iSize):
        Value = int(input("Enter element {}: ".format(i+1)))
        Arr.append(Value)
    print("Entered elements in sequence:",Arr)
    
    iRet = Diff(Arr,iSize)
    print(f"Difference is:{iRet}")
if __name__ == "__main__":
    main()