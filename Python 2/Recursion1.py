#1. Write a recursive program which accept string from user and count white
#spaces.
#Input : HE llo WOr lD
#Output : 3

def countspace(string):
    count = 0
    i = 0
    while(i < len(string)):
        if (string[i]==" "):
            count += 1
        i += 1
    print(count)

count = 0
i = 0
def countspace1(string):
    global count
    global i
    if(i < len(string)):
        if (string[i]==" "):
            count += 1
        i += 1
        countspace(string)
print(count)
def main():
    string = input("Enter a string:")

    countspace(string)
    countspace1(string)
if __name__ == "__main__":
    main()
