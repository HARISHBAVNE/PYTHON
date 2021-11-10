# 2. Accept Character from user and check whether it is capital or not
# (A-Z).
# Input : F
# Output : TRUE
# Input : d
# Output : FALSE

def Checkcapital(ch):
    if(ch >=ord('A')and ch <=ord('Z')):
        return True
    else:
        return False


def main():
    ch = ord(input("Enter a character:"))
    ret = Checkcapital(ch)
    if (ret == True):
        print("TRUE")
    else:
        print("FALSE")
    
if __name__ == "__main__":
    main()
