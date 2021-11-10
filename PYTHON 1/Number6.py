# 1.Write a program which accept number from user and print that number of $ & *
# on screen.
# Input : 5
# Output : $ * $ * $ * $ * $ *

def Pattern(No):
    if No < 0:
        No = -(No)
    for i in range(No):
        print("$ * ",end = " ")

def main():
    No = int(input("Enter a number"))
    Pattern(No)
    
if __name__ == "__main__":
    main()