# 1. Accept N numbers from user and return frequency of even numbers.
# Input : N : 6
# Elements : 85 66 3 80 93 88
# Output : 3

def Frequency(Numbers):
    iCnt = 0
    for i in range(len(Numbers)):
        if Numbers[i]%2 == 0:
            iCnt += 1
    return iCnt

def main():
    Numbers = []
    size = int(input("Enter a number of elements:"))
    print("Enter elements")
    
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    Ret = Frequency(Numbers)
    print("Frequency of even number is:",Ret)
if __name__ == "__main__":
    main()