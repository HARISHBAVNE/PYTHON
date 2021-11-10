# 3. Write  program which accept N numbers from user and accept
# one another number as NO , return index of last occurrence of that NO.
# Input : N : 6                           Input : N : 6                               
# NO: 66                                  NO: 12
# Elements : 85 66 3 66 93 88             Elements : 85 11 3 15 11 111
# Output : 3                              Output : -1




#=================
# Function 
#=================
def LastOcc(Arr,No):
    check = 0
    for i in range(len(Arr)):
        if (Arr[i] == No):
            check = i
    if (check == 0):
        return -1
    else:
        return check
        
    
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
    
    No = int(input("Enter a numbr:"))
    
    Ret = LastOcc(Arr,No)
    print(f"Index of Last occurrence of that no. is:{Ret}")
if __name__ == "__main__":
    main()
