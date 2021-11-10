# 1. Write a recursive program which display below pattern.
# Output : * * * * *

def Display(No):
    while (No>0):
        print("*\t",end = " ")
        No -= 1
    
def DisplayR(No):
    if (No>0):
        print("*\t",end = " ")
        Display(No-1)
def main():
    No = int(input("Enter a number"))
    DisplayR(No)


if __name__ == "__main__":
    main()
