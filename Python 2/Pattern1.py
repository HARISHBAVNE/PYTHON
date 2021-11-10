# 1. Accept number from user and display below pattern.
# Input : 5
# Output : A B C D E

def Pattern(No):
    ch = ord('A')
    for i in range(0,5):
        print(chr(ch+i),end = " ")
def main():
    No = int(input("Enter a number:"))
    Pattern(No)
    
if __name__ == "__main__":
    main()