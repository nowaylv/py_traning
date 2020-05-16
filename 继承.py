class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


class Cat(Animal):

    def __init__(self, name):
        #super().__init__(name不可以写多行
        super().__init__(name)#继承父类的初始话函数


cat1 = Cat("大白")
cat1.show()

#self training 
print("\n--------------self training-----------------")
#-----------------多态-----------------
class super_class:
    def show(self):
        print("i am super_class")

class soon_class:
    def show(self):
        print("i am soon class")

class other:
    def show(self):
        print("i dont know")

def display(super_class):
    super_class.show()

super_class_demo = super_class()
soon_class_demo = soon_class()
other_demo = other()

display(super_class_demo)
#可以传入他的子类
display(soon_class_demo)
#也可以传入其他，只要他有show就行
display(other_demo)
