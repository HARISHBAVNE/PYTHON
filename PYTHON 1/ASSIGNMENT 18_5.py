# 5. Accept N numbers from user and accept one another number as NO ,
# return frequency of NO form it.
# Input : N : 6
# NO: 66
# Elements : 85 66 3 66 93 88
# Output : 2
# Input : N : 6
# NO: 12
# Elements : 85 11 3 15 11 111
# Output : 0
def Frequency(Numbers,No):
    iCnt = 0
    for i in range(len(Numbers)):
        if Numbers[i] == No:
            iCnt += 1
    return iCnt
def main():
    Numbers = []
    size = int(input("Enter a number of elements:"))
    print("Enter elements")
    
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    No = int(input("Enter a number that you want to search:"))
    Ret = Frequency(Numbers,No)
    print(Ret)
if __name__ == "__main__":
    main()