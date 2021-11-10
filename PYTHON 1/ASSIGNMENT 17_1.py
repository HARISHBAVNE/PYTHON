# 1. Accept N numbers from user and return difference between summation
# of even elements and summation of odd elements.
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 53 (234 - 181)

def Diff(Elements):
    Esum = 0
    Osum = 0
    for i in range(len(Elements)):
        if ((Elements[i]%2)==0):
            Esum += Elements[i]
        else:
            Osum += Elements[i]
    return (Esum - Osum)

def main():
    Numbers = []
    size = int(input("Enter number of elements:"))
    
    print("Enter a elements")
    for i in range(size):
        value = int(input("Element {}:".format(i+1)))
        Numbers.append(value)
    ret = Diff(Numbers)
    print("Difference between even and odd sum:",ret)
    
    
if __name__ == "__main__":
    main()