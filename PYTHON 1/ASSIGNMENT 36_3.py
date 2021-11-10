# 3.Write a recursive program which display below pattern.
# Output : 5 4 3 2 1

def Display(No):
    while (No>0):
        print(No,"\t",end = " ")
        No -= 1
    
def DisplayR(No):
  
    if (No>0):
        print(No,"\t",end = " ")
        #No -= 1
        Display(No-1)
def main():
    No = int(input("Enter a number"))
    DisplayR(No)


if __name__ == "__main__":
    main()
