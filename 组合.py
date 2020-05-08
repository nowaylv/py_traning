class Eye:

    def __init__(self, color):
        self.color = color


class Person:

    def __init__(self, eye):
        self.eye = eye

    def show(self):
        print(self.eye.color)


eye = Eye("黑色")
p = Person(eye)
p.show()

#self training 
print("\n--------------self training-----------------")

class base:
    def __init__(self, name):
        self.name = name

class other:
    def __init__(self, base):
        self.base = base

    def show(self):
        print(self.base.name)
        
base_demo = base("noway")
other_demo = other(base_demo)#可传入对象

other_demo.show()