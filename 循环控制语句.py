# 打印出0到9
for i in range(3, 10, 2):
    print(i, end=" ")

print("\n=======================")
# 遍历列表
a_list = {4, 5, 6, 7, 8, 9}
for a in a_list:
    print(a, end=" ")

print("\n=======================")
# 带索引的遍历
for i, a in enumerate(a_list):
    print(i, ":", a)

print("\n=======================")
# 遍历dict
b_dict = {"name": "zhang3", "sex": "男", "age": 36}
for key, value in b_dict.items():
    print(key, ":", value)

#self training 
print("\n--------------self training-----------------")
circle_ctrl_demo = ["faf", 'a', "reqr", "fafassaf", "fafq", "faffafa"]
for x, num in enumerate(circle_ctrl_demo):#return index and values
    print(x , ":", num)

dict_demo = {"name":"noway","eye":"black", "matherland":"China" }
for y, val in enumerate(dict_demo):
    print(y, "：", val)

for z, value in dict_demo.items():
    print(z, ";", value)

'''
#for可以迭代任意可迭代的对象，例如字符串，dict...
#判断是否能迭代
from collections import Iterable
isinstance("abs", Iterable)
'''

#可以用for生成一个列表，for之后可以加判断,但不能添加else
demo_list_for = [x**2 for x in range(0,13) if x % 5 == 0]
print(demo_list_for)

#----------------------------------两层循环----------------------------------
str_a = "abc"
str_b = "ABC"
str_c = []
for x in str_a:
    for y in str_b:
        str_c.append(x + y)

print(str_c[:])

#----------------------------------生成器----------------------------------
lan = [L * L for L in range(3,7)]
print(lan)

#生成器就是把上面的【】改为（）
generator_demo = (G*G for G in range(3,7))

for n in generator_demo:
    print(n)

#函数形式生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b#有yeild 关键字之后函数就是个生成器,yeild是generator执行的起点和终点
        a, b = b, a + b
        n += 1
    return 'done'

#调用
F = fib(10)#fib是个类，将他实例化

while True:
    try:
        print(next(F))
    except StopIteration as e:#捕获异常给e
        print(e.value)
        break

#----------------------------------迭代器----------------------------------
#生成器也是迭代器的一种
#常见可迭代类型list, tuple, set, str, generator,但前面四个不能称为迭代器,
# 因为iterator表示一种不断的数据流，而list等却不能无限大
#我们可以使用iter()来强制转化为迭代器
from collections import Iterator
list_iter_demo = [2, 2,4,5,3,3,3,11,2,3421,12]
list_iterator = iter(list_iter_demo)
print(isinstance((list_iterator), Iterator))

#list转化为iterator
for u in list_iterator:
    print(u)

