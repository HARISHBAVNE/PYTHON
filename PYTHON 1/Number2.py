# 2.Write a program which accept number from user and display its factors in
# decreasing order.
# Input : 12
# Output : 6 4 3 2 1

def DisplayFact(No):
    for i in range(int(No/2)+1,0,-1):
        if ((No%i) == 0):
            print(f"{i}",end = " ")
    

def main():
    No = int(input("Enter a number:"))
    DisplayFact(No)
   
if __name__ == "__main__":
    main()
