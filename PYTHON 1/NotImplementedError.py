class Animal:
    def __init__(self,name):
        self.name = name
    def details(self):
        raise NotImplementedError("You have to define method inside subclass only")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print("Bhow bhow")
    def details(self):
        print(f"Pet name is:{self.name}")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print("Meao")
    def details(self):
        print(f"Pet name is:{self.name}")
    
obj = Cat("Jimmy")
obj.sound()
obj.details()
