# 2. Accept number from user and display below pattern.
# Input : 5
# Output : 5 # 4 # 3 # 2 # 1 #

def Pattern(No):
    for i in range(No,0,-1):
        print(i," #",end = " ")
def main():
    No = int(input("Enter a number:"))
    Pattern(No)
    
if __name__ == "__main__":
    main()