#------------------------高阶函数------------------------
#变量也可以指向函数
absctrct = abs
print(absctrct(-90))

'''
#函数名起始就是指向函数的变量
import builtins;builtins.abs = 10
print (abs)
'''

#函数名可以作为变量传入参数，这就是函数的函数既高阶参数
def add(x, y, f):
    return f(x) + f(y)

print(add(-2, 3, abs))   

"""------------------------函数作为参数输入#------------------------"""
#------------------------map/reduce------------------------
#map既映射，map是Python的内建函数， 输入参数一个是函数，一个是可迭代对象
list_demo = [1,2,3,4,5,6,7,8,9]
def pow_3(x):
    return x**3

#可以看书map作用是将函数直接作用到一个可迭代对象上
print(list(map(pow_3, list_demo)))
#也可以使用匿名函数lambda,lambda也可以赋值给一个对象
print(list(map(lambda x: x**3, list_demo)))
'''匿名函数也可以给到变量也可以作为函数返回值'''

#reduce
#reduce(f, [x1, x2, x3, x4, x5, x6, x7]) = f(f(f(f(f(f(x1, x2), x3), x4), x5), x6), x7)
from functools import reduce
reduce_demo = [1,2,3,4,5,6,7]

def ADD(x, y):
    return x + y

print(reduce(ADD, reduce_demo))

#------------------------filter------------------------
#filter和map类似，传入参数一样， 作用是将可迭代对象的一部分元素过滤
#过滤取决于函数返回值（True?False）
filter_list = [2,3,5,6,3,6,3,6,7,89]
def reserve_odd(x):
    return x % 2 != 0

print(list(filter(reserve_odd, filter_list)))

"""------------------------函数作为返回值------------------------"""
def caculate_sum(*number):
    def add():
        sum = 0
        for n in number:
            sum += n
        return sum
    return add

#相关参数和变量都保存在返回的函数中
f1 = caculate_sum(1,2,3,455)#返回的是求和函数
print(f1())

#函数内还能可以嵌套定义返回函数的函数
def count():
    def func(j):
        def g():
            return j*j
        return g
    
    fs = []
    for i in range(1, 4):
        fs.append(func(i))
    return fs

f2, f3, f4 = count()
print(f4(), f2(), f3())

#------------------------sorted------------------------
#sorted函数是可以传入函数参数的
sorted_list = [-1,2,4,-42,90,-2,34,-98]

print(sorted(sorted_list, key=abs, reverse=True))

#------------------------装饰器------------------------
#装饰器，代码运行期间动态增加功能,装饰过后函数的__name__会改变
#函数也是一个对象
print(print.__name__)

def log(func):
    def wraper(*args, **kwargs):#可以接受任意参数
        print(func.__name__)
        return func(*args, **kwargs)
    return wraper


@log  # @log相当于demo_decrator = log(demo_decrator)s
def demo_decrator():
    print("fasf")

demo_decrator()
print(demo_decrator.__name__)#装饰后函数签名也会变

#如果装饰器本身需要传入参数
def log(stringer):
    def decorator(fun):
        def ce(*args, **kwargs):
            print(fun.__name__, stringer)
            return fun(*args, **kwargs)
        return ce
    return decorator

@log('ok')
def dec_param():
    print('i am dec param')

dec_param()
print(dec_param.__name__)#函数签名是ce

