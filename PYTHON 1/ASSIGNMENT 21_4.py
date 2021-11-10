# 4. Accept Character from user and check whether it is small case or
# not (a-z).
# Input : g
# Output : TRUE
# Input : D
# Output : FALSE

def CheckSmall(ch):
    if (ch >=ord('a') and ch <=ord('z') ):
        return True
    else:
        return False


def main():
    ch = ord(input("Enter a character:"))
    ret = CheckSmall(ch)
    if (ret == True):
        print("TRUE")
    else:
        print("FALSE")
    
if __name__ == "__main__":
    main()
