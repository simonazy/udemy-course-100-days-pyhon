def add(*args):
    print(args)
    print(type(args)) #tuple
    print(args[0])
    sum = 0
    for arg in args:
        sum += arg 
    return sum 

print(add(3,4,5,6,9))  

def calculate(n,**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k)
        print(v) 
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

    
calculate(2, add=5, multiply=3)

class Car:
    def __init__(self, **kwargs) -> None:
        self.model = kwargs.get("model")  #use get, instead of dict index
        self.make = kwargs.get("make") 
        self.seat = kwargs.get("seat") 

my_car = Car(seat = 5, model = "GT-R", make = "Nissan")
print(f"Model: {my_car.model} made by {my_car.make} has {my_car.seat}") 

another_car = Car(seat = 5, model = "GT-R")
print(f"Model: {another_car.model} made by {another_car.make} has {another_car.seat}") 