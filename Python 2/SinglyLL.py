
class Node:
    def __init__(self,No):
        self.Data = No
        self.Next = None

class SinglyLL:
    Size = 0;
    def __init__(self):
        self.Head = None
    
    def InsertFirst(self,No):
        newn = Node(No)
        newn.Next = None
        if (self.Head == None):
            self.Head = newn
            SinglyLL.Size += 1
        else:
            newn.Next = self.Head
            self.Head = newn
            SinglyLL.Size += 1
    def Display(self):
        temp = self.Head
        while(temp!= None):
            print(f"|{temp.Data}|","->",end = " ")
            temp = temp.Next
        print("NULL")
    def Count(self):
        return (SinglyLL.Size)
    def InsertLast(self,No):
        temp = self.Head
        newn = Node(No)
        if (self.Head == None):
            self.Head = newn
            SinglyLL.Size += 1
        else:
            while(temp.Next != None):
                temp = temp.Next
            temp.Next = newn
            SinglyLL.Size += 1
    def InsertAtPosition(self,No,Pos):
        newn = Node(No)
        temp = self.Head
        if (Pos < 1) or (Pos > SinglyLL.Size + 1):
            print("Enter a valid Position:")
        if (Pos == 1):
            InsertFirst(No)
        elif(Pos == SinglyLL.Size+1):
            InsertLast(No)
        else:
            for i in range(1,Pos-1):
                temp = temp.Next
            newn.Next = temp.Next
            temp.Next = newn
            SinglyLL.Size += 1
    def DeleteFirst(self):
        if (self.Head == None):
            return
        if (self.Head.Next == None):
            del(self.Head)
            self.Head = None
            SinglyLL.Size -= 1
        else:
            temp = self.Head
            self.Head = self.Head.Next
            del(temp)
            SinglyLL.Size -= 1
    def DeleteLast(self):
        if (self.Head == None):
            return
        if (self.Head.Next == None):
            del(self.Head)
            self.Head = None
            SinglyLL.Size -= 1
        else:
            temp = self.Head
            for i in range(1,SinglyLL.Size):
                temp = temp.Next
            del(temp.Next)
            temp.Next = None
            SinglyLL.Size -= 1
    def DeleteAtPosition(self,Pos):
        temp = self.Head
        if (Pos < 1) or (Pos > SinglyLL.Size):
            print("Enter a valid Position:")
        if (Pos == 1):
            DeleteFirst()
        elif(Pos == SinglyLL.Size):
            DeleteLast()
        else:
            for i in range(1,Pos-1):
                temp = temp.Next
            Target = temp.Next
            temp.Next = Target.Next
            del(Target)
            SinglyLL.Size -= 1


def main():
    obj = SinglyLL()
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
            obj.InsertAtPosition(No,pos)
        elif choice == 4:
            obj.DeleteFirst()
        elif choice == 5:
            obj.DeleteLast()
                
        elif choice == 6:
            pos = int(input("Enter a position"))
            obj.DeleteAtPosition(pos)
        elif choice == 7:
            obj.Display()
        elif choice == 8:
            ret =obj.Count()
            print("Number of nodes are:",ret)
        elif choice == 0:
            print("Thank you for using application")
            break
        else:
            print("Please Enter a Valid Choice from Menu")
        menu()
        choice = int(input("Enter your choice"))

if __name__ == "__main__":
    main()
