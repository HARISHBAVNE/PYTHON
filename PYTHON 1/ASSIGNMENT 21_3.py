# 3. Accept Character from user and check whether it is digit or not
# (0-9).
# Input : 7
# Output : TRUE
# Input : d
# Output : FALSE

def CheckDigit(ch):
    try:
        if(int(ch)):
            if((int(ch)>=0)and(int(ch)<=9)):
                return True
            else:
                return False
    except:
        return False


def main():
    ch = input("Enter a character:")
    ret = CheckDigit(ch)
    if (ret == True):
        print("TRUE")
    else:
        print("FALSE")
    
if __name__ == "__main__":
    main()
