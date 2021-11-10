# 5. Write  program which accept N numbers from user and return
# product of all odd elements.
# Input : N : 6
# Elements : 15 66 3 70 10 88
# Output : 45
# Input : N : 6
# Elements : 44 66 72 70 10 88
# Output : 0



#=================
# Function 
#=================
def Product(Arr):
    OddMult = 1
    for i in range(len(Arr)):
        if ((Arr[i]%2) != 0):
            OddMult = OddMult * Arr[i]
    if (OddMult == 1):
        return 0
    else:
        return OddMult
        
    
#==================
#Main Satrter.
#==================
def main():
    iSize = int(input("Enter a number of elements:"))
    Arr = []
    print("Enter elements")
    for i in range (1,iSize+1):
        value = int(input(f"Enter element No{i}:"))
        Arr.append(value)
    
    
    Ret = Product(Arr)
    print(f"product of all odd elements is:{Ret}")
if __name__ == "__main__":
    main()
