# 1. Accept N numbers from user and return the largest number.
# Input : N : 6
# Elements : 85 66 3 66 93 88
# Output : 93

def Largest(Arr,iSize):
    maxi = Arr[0]
    for i in range(iSize):
        if (Arr[i]>maxi):
            maxi = Arr[i]
    return maxi
def main():
    print("Enter Number of elements")
    iSize = int(input())
    Arr = []
    print("Enter elements")
    for i in range(iSize):
        Value = int(input("Enter element {}: ".format(i+1)))
        Arr.append(Value)
    print("Entered elements in sequence:",Arr)
    
    iRet = Largest(Arr,iSize)
    print(f"Largest number from sequence is:{iRet}")
if __name__ == "__main__":
    main()