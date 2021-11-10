# 5. Accept number from user and display below pattern.
# Input : 8
# Output : 2 4 6 8 10 12 14 16

def Pattern(No):
    for i in range(1,No+1):
        print(i*2,end = " ")
def main():
    No = int(input("Enter a number:"))
    Pattern(No)
    
if __name__ == "__main__":
    main()