# 1.Write a program which accept range from user and display all numbers in between
# that range.
# Input : 23 35
# Output : 23 24 25 26 27 28 29 30 31 32 33 34 35
# Input : 10 18
# Output : 10 11 12 13 14 15 16 17 18
def DisplayRange(Start , Stop):
    if (Stop < Start):
        print("Invalid Range")
        exit()
    for i in range(Start,Stop+1):
        print(i,end = " ")


def main():
    No1 = int(input("Enter a Start point:"))
    No2 = int(input("Enter a Stop point:"))
    DisplayRange(No1,No2)
if __name__ == "__main__":
    main()