# 2. Write a program which accept range from user and display all even numbers in
# between that range.
# Input : 23 35
# Output : 24 26 28 30 32 34
# Input : 10 18
# Output : 10 12 14 16 18
# Input : 10 10
# Output : 10
# Input : -10 2
# Output : -10 -8 -6 -4 -2 0 2
class Even:
    def __init__(self,no1,no2):
        self.Start = no1
        self.Stop = no2
    def DisplayRange(self):
        if (self.Stop < self.Start):
            print("Invalid Range")
            exit()
        for i in range(self.Start,self.Stop+1):
            if ((i%2)==0):
                print(i,end = " ")


def main():
    No1 = int(input("Enter a Start point:"))
    No2 = int(input("Enter a Stop point:"))
    
    obj = Even(No1,No2)
    obj.DisplayRange()
if __name__ == "__main__":
    main()