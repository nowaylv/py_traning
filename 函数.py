# 定义一个加法函数
def add(a, b):
    c = a + b
    return c


if __name__ == '__main__':
    # 调用一个加法函数
    d = add(3, 5)
    print(d)

#------------------------self training------------------------
print("\n----------self training-------------")

def func_demo(a, b):
    print("i am a function")
    return a ** b


demo_value_1 = 2
demo_value_2 = 2
print(func_demo(demo_value_1, demo_value_1))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
function = func_demo
print(function(demo_value_1, demo_value_2))

#max内建函数可以传入多个参数
print(max(2,-1,90,89,898989,99999))

#定义过后的函数可以在其他文件被导入
#from 函数 import func_demo

#------------------------与C语言不一样可以返回多个参数------------------------
def multi_return(a, b):
#Python输入参数不会检查类型所以自己要判断一下
    if  isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a, b
    
print(multi_return(2, 3))
    
#------------------------默认参数,默认要放在后面------------------------
def print_information(name, sex = "male", age = 17, area = "China"):
    print("name:", name, "\r\n")
    print("sex:", sex, "\r\n")
    print("age:", age, "\r\n")
    print("area", area, "\r\n")

#只需输入一个参数
print_information("noway")
print_information("hfad", "female")
#如需不按照定义顺序改变某个默认参数必须指定变量名
print_information("noway", age = 18)

#------------------------可变参数，参数个数可以变------------------------
#*params表示把params作为可变参数传进去
def variable_param(*params):
    var_sum = 0#局部变量需要先声明
    for x in params:
        var_sum += x
    
    print(var_sum)
#不用[]
variable_param(2,3,4,5,6,7)
#也可以这么调用,*list
varsity= (1,2,3,4,5,6,7)#tuple也可以
variable_param(*varsity)

#------------------------关键字参数------------------------ 
#**other可以添加更多默认参数
def key_param(name, age, **other):
    print("name:", name, "age:", age, "other:", other)

key_param("noway", 18)

#------------------------ 相当于添加多个指定默认参数------------------------ 
training = {"area":"CH", "work":"enginer"}
key_param("noway", 18, area = "CH", work = "enginer")
key_param("nway", 18, **training)#调用和可变参数类似

#------------------------ 命名关键字参数------------------------ 
def name_key(name, age, *, city = "wuhu", language):#'*'后面表示都是关键字参数,也可加默认值
    print(name, age, city, language)

name_key("noway", 18, language = "chinese")#调用是要

#------------------------参数组合------------------------
#参数定义顺序必须是必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1,2)
f1(1, 2, 3, "a", "b")

#------------------------偏函数------------------------
#当函数参数较多，某一个函数不需重复赋值的时候可以采用偏函数
import functools
partial_fun = functools.partial(int, base = 2)
print(partial_fun('010101'))
