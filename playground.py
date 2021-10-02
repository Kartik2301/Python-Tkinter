def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(4,8,54,100,2,3,6,8,9))

def calculate(n,**kwargs):
    # for (key, val) in kwargs.items():
    #     print(key, val)
    # print(kwargs["add"])
    n += kwargs.get("add")
    n *= kwargs.get("mult")
    return n

print(calculate(2,add=5, mult=7))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.colour = kwargs.get("colour")
        self.model = kwargs.get("model")
        self.seats = kwargs.get("seats")

car = Car(make="Nissan", colour="red", model="GT-R", seats=4)
print(car.make, car.colour, car.model, car.seats)