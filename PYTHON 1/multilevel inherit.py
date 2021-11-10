class Father:
    def __init__(self,car):
        self.car = car
    def vehicle(self):
        print(self.car)

class Son(Father):
    def __init__(self,car,bike):
        Father. __init__(self,car)
        self.bike = bike
    def Vehicles(self):
        print(self.car,self.bike)

class GrandSon(Son):
    def __init__(self,car,bike,cycle):
        Son. __init__(self,car,bike)
        self.cycle = cycle
    def Vehicles1(self):
        print(self.car,self.bike,self.cycle)

def main():
    
    obj = GrandSon("BMW","Hero","Atlas")
    obj.vehicle()
    obj.Vehicles1()

if __name__ == "__main__":
    main()
