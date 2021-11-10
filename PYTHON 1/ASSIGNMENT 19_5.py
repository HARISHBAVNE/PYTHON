# 5. Accept N numbers from user and return product of all odd elements.
# Input : N : 6
# Elements : 15 66 3 70 10 88
# Output : 45
# Input : N : 6
# Elements : 44 66 72 70 10 88
# Output : 0
def Occurence(Numbers):
    Mult = 1
    flag = 0
    for i in range(len(Numbers)):
        if ((Numbers[i]%2)!=0):
            flag = 1
            Mult = Mult * Numbers[i]
    if(flag == 0):
        return 0
    else:
        return Mult
            
def main():
    Numbers = []
    size = int(input("Enter a number of element:"))
    
    print("Enter a elements")
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    
    Ret = Occurence(Numbers)
    print(Ret)
    
if __name__ == "__main__":
    main()