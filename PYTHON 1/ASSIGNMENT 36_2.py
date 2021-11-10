# 2. Write a recursive program which display below pattern.
# Output : 1 2 3 4 5

def Display(No):
    i = 1
    while (i<=No):
        print(i,"\t",end = " ")
        i += 1
    
def DisplayR(No):
    i = 1
    if (i<=No):
        print(i,"\t",end = " ")
        i +=1
        Display(No)
def main():
    No = int(input("Enter a number"))
    DisplayR(No)


if __name__ == "__main__":
    main()
