# 数的类型转换
a = 1
print(type(a))
b = a
print(type(b), b)
b = float(a)
print(type(b), b)

print("=============================")
# 集合类型转换
c = [1, 2, 3]
print(type(c))
d = tuple(c)    
print(type(d))

print("=============================")
# 利用类型转换去掉列表中重复元素
e = [1, 1, 2, 2, 3, 3]
print(e)
print(list(set(e)))

#self training 
print("\n--------------self training-----------------")

type_demo = "adfadsf"
type_demo_1 = 89421941
type_demo_2 = 32.2
type_name_q = type(type_demo_2)
print(type_name_q)

print(type_name_q(type_demo_1))
#type_list = list(type_demo_1)#集合与变量之间不能转化

demo_tuple = (2, 2, 42, 6, 424, 525,666, 7732,27)#元组排序
demo_list = list(demo_tuple)
demo_list.sort()
demo_tuple = tuple(demo_list)
print(demo_tuple)