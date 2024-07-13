class car:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def car_name(self):
     print("my car name is",self.name)
class bike(car):
     pass
c1=bike("Honda",2020)
print(c1.name)
c1.car_name()
