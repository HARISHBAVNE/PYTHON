# 3. Write a program which accept number from user and print its numbers line.
# Input : 4
# Output : -4 -3 -2 -1 0 1 2 3 4

def Display(No):
    for i in range(-No,No+1):
        print(i,end = " ")

def main():
    No = int(input("Enter a number:"))
    Display(No)
if __name__ == "__main__":
    main()