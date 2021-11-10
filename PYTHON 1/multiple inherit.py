class Father:
    def __init__(self,car):
        self.car = car
    def vehicle(self):
        print(self.car)

class Mother:
    def __init__(self,scooty):
        self.scooty = scooty 
    def vehicle(self):
        print(self.scooty)

class Son(Mother,Father):
    def __init__(self,car,scooty):
        Father. __init__(self,car)
        Mother. __init__(self,scooty)


def main():
    
    obj = Son("BMW","Hero")
    obj.vehicle()

if __name__ == "__main__":
    main()
