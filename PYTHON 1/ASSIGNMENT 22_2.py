# 2. Accept character from user. If character is small display its
# corresponding capital character, and if it small then display its
# corresponding capital. In other cases display as it is.
# Input : Q
# Output : q
# Input : m
# Output : M
# Input : 4
# Output : 4 

def Display(ch):
    if (ord(ch) >=ord("A") and ord(ch) <=ord("Z")):
        print(chr(ord(ch)+32))
    elif (ord(ch) >=ord("a") and ord(ch) <=ord("z")):
        print(chr(ord(ch)-32))
    else:
        print(ch)
def main():
    ch = input("Enter a character:")
    Display(ch)
    
if __name__ == "__main__":
    main()
