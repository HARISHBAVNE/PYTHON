# 1. Accept N numbers from user and accept one another number as NO ,
# check whether NO is present or not.
# Input : N : 6
# NO: 66
# Elements : 85 66 3 66 93 88
# Output : TRUE
# Input : N : 6
# NO: 12
# Elements : 85 11 3 15 11 111
# Output : FALSE

def Check(Numbers,No):
    for i in range(len(Numbers)):
        if Numbers[i] == No:
            return True
            break
    else:
        return False

def main():
    Numbers = []
    size = int(input("Enter a number of element:"))
    
    print("Enter a elements")
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    No = int(input("Enter a number that you want to search:"))
    ret = Check(Numbers,No)
    if (ret == True):
        print("TRUE")
    else:
        print("FALSE")
    
if __name__ == "__main__":
    main()