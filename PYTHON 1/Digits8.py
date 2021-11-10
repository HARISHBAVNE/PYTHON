# 3.Write a program which accept number from user and return the count of digits in
# between 3 and 7.
# Input : 2395
# Output : 1
# Input : 1018
# Output : 0
# Input : 4521
# Output : 2

def Count(No):
    count = 0
    if (No < 0):
        No = -(No)
    while(No > 0):
        if ((No%10) > 3) and ((No%10) < 7):
            count += 1
        No = No//10
    return count

def main():
    No = int(input("Enter a number:"))
    ret = Count(No)
    print(f"Digits in between 3 and 7 are:{ret}")

if __name__ == "__main__":
    main()
