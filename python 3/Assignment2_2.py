#2. Write a program which accept one number and display below pattern.
#nput : 5
#Output : * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *


#solution

def Spattern(value):
    for row in range(value):
        for col in range(value):
            print("* ", end = " ")
        print()

def main():
    print("Enter a number to print pattern")
    num = int(input())
    ans = Spattern(num)

#Code starter
if __name__ == "__main__":
    main()
