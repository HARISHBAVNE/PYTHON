# 1. Write program which accept N numbers from user and accept
# one another number as NO , check whether NO is present or not.
# Input : N : 6                              Input : N : 6
# NO: 66                                     NO: 12 
# Elements : 85 66 3 66 93 88                Elements : 85 11 3 15 11 111   
# Output : TRUE                              Output : FALSE

#=================
# Function 
#=================
def Check(Arr,No):
    check = 0
    for i in Arr:
        if (i == No):
            check = 1
            break
    if (check == 1):
        return True
    else:
        return False
    
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
    
    Ret = Check(Arr,No)
    if (Ret == True):
        print("TRUE")
    else:
        print("FALSE")
if __name__ == "__main__":
    main()
