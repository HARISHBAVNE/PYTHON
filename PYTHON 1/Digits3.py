# 3.Write a program which accept number from user and count frequency of 2 in it.
# Input : 2395
# Output : 1
# Input : 1018
# Output : 0
# Input : 9000
# Output : 0
# Input : 922432
# Output : 3

def Count(No):
    count = 0
    while(No > 0):
        if ((No%10) == 2):
            count += 1
        No = No//10
    return count

def main():
    No = int(input("Enter a number:"))
    ret = Count(No)
    print(f"Occuerence of 2 is:{ret}")

if __name__ == "__main__":
    main()