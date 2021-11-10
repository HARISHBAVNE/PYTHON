# 2. Accept N numbers from user and accept one another number as NO ,
# return index of first occurrence of that NO.
# Input : N : 6
# NO: 66
# Elements : 85 66 3 66 93 88
# Output : 1
# Input : N : 6
# NO: 12
# Elements : 85 11 3 15 11 111
# Output : -1

def Occurence(Numbers,No):
    for i in range(len(Numbers)):
        if Numbers[i] == No:
            return i
            break
    else:
        return "Not present."

def main():
    Numbers = []
    size = int(input("Enter a number of element:"))
    
    print("Enter a elements")
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    No = int(input("Enter a number that you want to search:"))
    ret = Occurence(Numbers,No)
    print(ret)
    
    
if __name__ == "__main__":
    main()