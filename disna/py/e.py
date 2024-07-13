class Parent:
    def func1(self):
        print("this is function is in parent class")
class Child(Parent):
     def func2(self):
         print("this is function is in child class")
obj=Child()
obj.func1()
obj.func2()
