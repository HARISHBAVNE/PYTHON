#1. Accept Character from user and check whether it is alphabet or not
#(A-Z a-z).
#Input : F
#Output : TRUE
#Input : &
#Output : FALSE

def CheckAlpha(ch):
    if(ch >=ord('A')and ch <=ord('Z'))or(ch >=ord('a')and ch <=ord('z')):
        return True
    else:
        return False


def main():
    ch = ord(input("Enter a character:"))
    ret = CheckAlpha(ch)
    if (ret == True):
        print("TRUE")
    else:
        print("FALSE")
    
if __name__ == "__main__":
    main()
