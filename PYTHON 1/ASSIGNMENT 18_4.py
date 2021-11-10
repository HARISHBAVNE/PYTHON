# 4. Accept N numbers from user and return frequency of 11 form it.
# Input : N : 6
# Elements : 85 66 3 15 93 88
# Output : 0
# Input : N : 6
# Elements : 85 11 3 15 11 111
# Output : 2

def Frequency(Numbers):
    iCnt = 0
    for i in range(len(Numbers)):
        if Numbers[i] == 11:
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
    print(Ret)
if __name__ == "__main__":
    main()