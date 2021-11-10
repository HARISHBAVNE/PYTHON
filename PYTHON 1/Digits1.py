# 1.Write a program which accept number from user and display its digits in reverse
# order.
# Input : 2395
# Output : 5
# 9
# 3
# 2

def DisplayDIgits(No):
    
    while(No > 0):
        print(No%10)
        No = No//10
    

def main():
    No = int(input("Enter a number:"))
    DisplayDIgits(No)


if __name__ == "__main__":
    main()