# 4.Write a program which accept number from user and count frequency of 4 in it.
# Input : 2395
# Output : 0
# Input : 1018
# Output : 0
# Input : 9440
# Output : 2
def Count(No):
    count = 0
    while(No > 0):
        if ((No%10) == 4):
            count += 1
        No = No//10
    return count

def main():
    No = int(input("Enter a number:"))
    ret = Count(No)
    print(f"Occuerence of 4 is:{ret}")

if __name__ == "__main__":
    main()