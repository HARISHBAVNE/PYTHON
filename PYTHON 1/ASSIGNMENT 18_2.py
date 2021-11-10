# 2. Accept N numbers from user and return difference between frequency of
# even number and odd numbers.
# Input : N : 7
# Elements : 85 66 3 80 93 88 90
# Output : 1 (4 -3)

def Frequency(Numbers):
    ECnt = 0
    OCnt = 0
    for i in range(len(Numbers)):
        if Numbers[i]%2 == 0:
            ECnt += 1
        else:
            OCnt += 1
    return (ECnt - OCnt)

def main():
    Numbers = []
    size = int(input("Enter a number of elements:"))
    print("Enter elements")
    
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    Ret = Frequency(Numbers)
    print(Ret)
if __name__ == "__main__":
    main()