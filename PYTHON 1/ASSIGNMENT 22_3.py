# 3. Accept character from user. If it is capital then display all the
# characters from the input characters till Z. If input character is small
# then print all the characters in reverse order till a. In other cases
# return directly.
# Input : Q
# Output : Q R S T U V W X Y Z
# Input : m
# Output : m l k j i h g f e d c b a
# Input : 8
# Output :

def Display(ch):
    if (ord(ch) >=ord("A") and ord(ch) <=ord("Z")):
        while(ord(ch)<=ord("Z")):
            print(ch,end=" ")
            ch = chr(ord(ch)+1)
    elif (ord(ch) >=ord("a") and ord(ch) <=ord("z")):
        while(ord(ch)<=ord("z")):
            print(ch,end=" ")
            ch = chr(ord(ch)+1)
def main():
    ch = input("Enter a character:")
    Display(ch)
    
if __name__ == "__main__":
    main()
