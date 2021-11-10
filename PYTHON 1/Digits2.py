# 2.Write a program which accept number from user and check whether it contains 0
# in it or not.
# Input : 2395
# Output : There is no Zero
# Input : 1018
# Output : It Contains Zero

def DisplayDIgits(No):
    
    while(No > 0):
        if ((No%10) == 0):
            return True
            break
        No = No//10
    

def main():
    No = int(input("Enter a number:"))
    ret = DisplayDIgits(No)
    if (ret == True):
        print("It contains Zero.")
    else:
        print("There is no Zero.")

if __name__ == "__main__":
    main()