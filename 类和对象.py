# 创建一个人类
class Person:
    pass

# 实例化一个人类
p = Person()

#self training 
print("\n--------------self training-----------------")
print(__name__)
#类中定义的函数必须第一个参数是self

#数据保护
#python通过‘__’前缀实现变量私有化
class demo:
    #可以专门为类创建属性，但对象都可访问修改s
    time = 20201010
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

demo_l = demo('noway', 90)

print(demo_l.get_age())

#这里修改的并不是__age，相当于新建了一个属性__age, 原来哪个__age已被解释成demo_l_age
demo_l.__age = 0
print(demo_l.get_age())

#dir()可以返回对象的所有属性和方法
print(dir(demo_l))

print(demo_l.time)
demo_l.time = 909090#可修改
print(demo_l.time)