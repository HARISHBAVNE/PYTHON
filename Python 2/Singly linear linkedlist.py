class node:
    def __init__(self,data):
        self.Data = data
        self.Next = None

class LinkedList:
    Size = 0
    def __init__(self):
        self.Head = None
    def InsertFirst(self,No):
        Newn = node(No)
        if (self.Head == None):
            self.Head = Newn
        else:
            Newn.Next = self.Head
            self.Head = Newn
        LinkedList.Size += 1
    def InsertLast(self,No):
        Newn = node(No)
        temp = self.Head
        if (self.Head == None):
            self.Head = Newn
        else:
            while(temp.Next!=None):
                temp = temp.Next
            temp.Next = Newn
        LinkedList.Size += 1

    def InsertAtPos(self,No,pos):
        Newn = node(No)
        if (pos < 1)or(pos > LinkedList.Size+1):
            print("Please provide valid position.")
            exit()
        if (self.Head == None):
            self.Head = Newn
            LinkedList.Size += 1
        elif (pos == 1):
            self.InsertFirst(No)
        elif (pos == LinkedList.Size+1):
            self.InsertLast(No)
        else:
            temp = self.Head
            for i in range(1,pos-1):
                temp = temp.Next
            Newn.Next = temp.Next
            temp.Next = Newn
            LinkedList.Size += 1

    def DeleteFirst(self):
        temp = self.Head
        if (self.Head == None):
            exit()
        else:
            self.Head = temp.Next
            del(temp)
            LinkedList.Size -= 1
    def DeleteLast(self):
        temp = self.Head
        if (self.Head == None):
            exit()
        else:
            if (temp.Next == None):
                self.Head = None
                del(temp)
            else:
                while(temp.Next.Next != None):
                    temp = temp.Next
                del(temp.Next)
                temp.Next = None
            LinkedList.Size -= 1

    def DeleteAtPos(self,pos):
        temp = self.Head
        if (pos < 1) or (pos > LinkedList.Size):
            exit()
        if (pos == 1):
            self.DeleteFirst()
        elif (pos == LinkedList.Size):
            self.DeleteLast()
        else:
            for i in range(1,pos-1):
                temp = temp.Next
            target = temp.Next
            temp.Next = target.Next
            del(target)
            LinkedList.Size -= 1



    def Display(self):
        temp = self.Head
        while(temp!= None):
            print("|",temp.Data,"|",end="->")
            temp = temp.Next
        print("None")
        print()
    def Count(self):
        return (LinkedList.Size)


def main():
    obj = LinkedList()

    def menu():
        print("*********************************")
        print("1:Insert First")
        print("2:Insert last")
        print("3:Insert at Position")
        print("4:DeleteFirst ")
        print("5:DeleteLast")
        print("6:DeleteAtPosition")
        print("7:Display element")
        print("8:Count Number of Nodes")
        print("0:Exit application")
        print("*********************************")

    menu()
    choice = int(input("Enter your choice"))

    while choice != 0:
        if choice == 1:
            No = int(input("Enter a number"))
            obj.InsertFirst(No)
        elif choice == 2:
            No = int(input("Enter a number"))
            obj.InsertLast(No)

        elif choice == 3:
            pos = int(input("Enter a position"))
            No = int(input("Enter a number"))
            obj.InsertAtPosition(No, pos)
        if choice == 4:
            obj.DeleteFirst()
        elif choice == 5:
            obj.DeleteLast()

        elif choice == 6:
            pos = int(input("Enter a position"))
            obj.DeleteAtPosition(pos)
        elif choice == 7:
            obj.Display()
        elif choice == 8:
            ret = obj.Count()
            print("Number of nodes are:", ret)
        elif choice == 0:
            print("Thank you for using application")
            break
        else:
            print("Please Enter a Valid Choice from Menu")
        menu()
        choice = int(input("Enter your choice"))

if __name__ == "__main__":
    main()