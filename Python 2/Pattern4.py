# 4. Accept number from user and display below pattern.
# Input : 4
# Output : # 1 * # 2 * # 3 * # 4 *

def Pattern(No):
    for i in range(1,No+1):
        print("#",i,"*",end = " ")
def main():
    No = int(input("Enter a number:"))
    Pattern(No)
    
if __name__ == "__main__":
    main()