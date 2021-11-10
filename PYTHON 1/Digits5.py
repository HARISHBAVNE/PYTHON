#5.Write a program which accept number from user and count frequency of such a
#digits which are less than 6.
#Input : 2395
#Output : 3
#Input : 1018
#Output : 3

def Count(No):
    count = 0
    while(No > 0):
        if ((No%10) < 6):
            count += 1
        No = No//10
    return count

def main():
    No = int(input("Enter a number:"))
    ret = Count(No)
    print(f"Occuerence of digits lesser than 6 is:{ret}")

if __name__ == "__main__":
    main()
