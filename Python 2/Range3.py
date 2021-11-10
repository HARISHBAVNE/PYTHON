# 3. Write a program which accept range from user and return addition of all numbers
# in between that range. (Range should contains positive numbers only)
# Input : 23 30
# Output : 212
# Input : 10 18
# Output : 126
# Input : -10 2
# Output : Invalid range
# Input : 90 18
# Output : Invalid range
class Add:
    def __init__(self,no1,no2):
        self.Start = no1
        self.Stop = no2
    def DisplayAdd(self):
        isum = 0
        if (self.Stop < self.Start) or (self.Start < 0) or (self.Stop < 0):
            print("Invalid Range")
            exit()
        for i in range(self.Start,self.Stop+1):
            isum += i
        return isum


def main():
    No1 = int(input("Enter a Start point:"))
    No2 = int(input("Enter a Stop point:"))
    
    obj = Add(No1,No2)
    print(obj.DisplayAdd())
if __name__ == "__main__":
    main()