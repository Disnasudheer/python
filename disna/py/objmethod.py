class Car:
 def __init__(self,name,year):
        self.fname=name
        self.lyear=year
 def car_name(self):
    print("my car name is:",self.fname)
c1=Car("honda",2020)
del c1.year
print(c1.year)
c1.car_name()
