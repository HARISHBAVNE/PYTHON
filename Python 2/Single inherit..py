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

def main():
    
    obj = Son("BMW","Hero")
    obj.vehicle()
    obj.Vehicles()

if __name__ == "__main__":
    main()
