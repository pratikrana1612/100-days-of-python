def add(*args):
    print(args)
    total=0
    for num in args:
        total+=num
    print(total)


def calculate(n,**kwargs):
    # print(type(kwargs))
    n+=kwargs['add']
    n*=kwargs['multipy']
    print(n)
    # for (key,value) in kwargs.items():
    #     print(key,value)

add(3,4,2,5,1,6,3,4,2)
calculate(5,add=3,multipy=4)

class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get('model')
        self.model=kw.get('color')
        self.model=kw.get('seats')


my_car=Car(make="car")
print(my_car.model)