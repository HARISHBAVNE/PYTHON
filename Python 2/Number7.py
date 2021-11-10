# 2.Write a program which accept number from user and print numbers till that
# number.
# Input : 8
# Output : 1 2 3 4 5 6 7 8

def Display(No):
    if (No < 0):
        No = -(No)
    i = 1    
    while(i <= No):
        print(i,end=" ")
        i += 1
    

def main():
    No = int(input("Enter a Number:"))
    Display(No)
    
if __name__ == "__main__":
    main()