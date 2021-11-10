# 5. Write a program which accept N and print first 5 multiples of N.
# Input : 4
# Output : 4 8 12 16 20

def Displayodd(No):
    for i in range(1,6):
        print(i*No,end = " ")
        

def main():
    No = int(input("Enter a number:"))
    Displayodd(No)
if __name__ == "__main__":
    main()