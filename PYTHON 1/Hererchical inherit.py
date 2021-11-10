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

class Daughter(Father):
    def __init__(self,car,scooty):
        Father. __init__(self,car)
        self.scooty = scooty
    def Vehicles1(self):
        print(self.car,self.scooty)

def main():
    
    obj = Daughter("BMW","Hero")
    obj.vehicle()
    obj.Vehicles1()

    obj1 = Son("BMW","Suzuki")
    obj1.vehicle()
    obj1.Vehicles()

if __name__ == "__main__":
    main()
