# 3. Accept N numbers from user check whether that numbers contains 11 in
# it or not.
# Input : N : 6
# Elements : 85 66 11 80 93 88
# Output : 11 is present

def Check(Numbers):
    flag = 0
    for i in range(len(Numbers)):
        if Numbers[i] == 11:
            return True
            break
    else:
        return False
def main():
    Numbers = []
    size = int(input("Enter a number of elements:"))
    print("Enter elements")
    
    for i in range(size):
        value = int(input(f"Element {i+1}:"))
        Numbers.append(value)
    Ret = Check(Numbers)
    if (Ret == True):
        print("11 is Present.")
    else:
        print("11 is not present.")
if __name__ == "__main__":
    main()