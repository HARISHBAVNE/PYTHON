# 4. Write a program which accepts N from user and print all odd numbers up to N.
# Input : 18
# Output : 1 3 5 7 9 11 13

def Displayodd(No):
    for i in range(No):
        if ((i%2)!= 0):
            print(i,end=" ")


def main():
    No = int(input("Enter a number:"))
    Displayodd(No)
if __name__ == "__main__":
    main()