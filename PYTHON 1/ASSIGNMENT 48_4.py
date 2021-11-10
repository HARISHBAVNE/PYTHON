# 4. Write program which accept N numbers from user and accept
# Range, Display all elements from that range
# Input : N : 6
# Start: 60
# End : 90
# Elements : 85 66 3 76 93 88
# Output : 66 76 88




#=================
# Function 
#=================
def Display(Arr,No1,No2):
    check = 0
    for i in range(len(Arr)):
        if (Arr[i]>No1) and (Arr[i]<No2):
            print(Arr[i],end = "  ")
            
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
    
    No1 = int(input("Enter a Start range:"))
    No2 = int(input("Enter a End range:"))
    Display(Arr,No1,No2)
   
if __name__ == "__main__":
    main()
