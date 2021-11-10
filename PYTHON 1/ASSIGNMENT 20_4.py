# 4. Accept N numbers from user and display all such numbers which contains
# 3 digits in it.
# Input : N : 6
# Elements : 8225 665 3 76 953 858
# Output : 665 953 858
def Display(Arr,Size):
    for i in range(Size):
        if ((Arr[i]>99)and(Arr[i]<999)):
            print(Arr[i],end=" ")

def main():
    iSize = int(input("Enter number of elements:"))
    Arr = []
    print("Enter Elements")
    for i in range(iSize):
        value = int(input(f"Enter element{i+1}:"))
        Arr.append(value)
    Display(Arr,iSize)
if __name__ == "__main__":
    main()