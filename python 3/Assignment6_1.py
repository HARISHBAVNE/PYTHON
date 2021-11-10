# 1.Write a program which contains one class named as Demo. Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value. There are two instance methods of class as Fun and Gun which displays values of instance
# variables. Initialise instance variable in init method by accepting the values from user. After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()
class Demo():
    Value = 10
    def __init__(self,i,j):
        self.no1 = i
        self.no2 = j
    def Fun(self):
        return self.no1,self.no2
        
    def Gun(self):
        return self.no1,self.no2

def main():
    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    Value3 = int(input("Enter third number: "))
    Value4 = int(input("Enter fourth number: "))
   
    obj1 = Demo(Value1,Value2)
    obj2 = Demo(Value3,Value4)
    
    ret = obj1.Fun()
    print("Obj1 Fun is: ",ret)
    ret = obj2.Fun()
    print("Obj2 Fun is: ",ret)
    ret = obj1.Gun()
    print("Obj1 Gun is:",ret)
    ret = obj2.Gun()
    print("Obj2 Gun is:",ret)
    print(Demo.Value)
    
if __name__ =="__main__":
    main()
