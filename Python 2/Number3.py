# 3.Write a program which accept number from user and display all its non factors.
# Input : 12
# Output : 5 7 8 9 10 11

def DisplayNonFact(No):
    for i in range(1,No):
        if ((No%i) != 0):
            print(f"{i}",end = " ")
    

def main():
    No = int(input("Enter a number:"))
    DisplayNonFact(No)
   
if __name__ == "__main__":
    main()
