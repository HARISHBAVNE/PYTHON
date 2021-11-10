# 4. Accept Character from user and check whether it is special symbol
# or not (!, @, #, $, %, ^, &, *).
# Input : %
# Output : TRUE
# Input : d
# Output : FALSE

def Display(ch):
    if (ord(ch) ==ord("!") or ord(ch) ==ord("@")or ord(ch) ==ord("#")or ord(ch) ==ord("$")or ord(ch) ==ord("%")or ord(ch) ==ord("^")or ord(ch) ==ord("&")or ord(ch) ==ord("*")):
        return True
    else:
        return FALSE
def main():
    ch = input("Enter a character:")
    ret = Display(ch)
    if (ret == True):
        print("TRUE")
    else:
        print("FALSE")
if __name__ == "__main__":
    main()
