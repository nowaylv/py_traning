a = 1  # 定义一个a变量，并赋值为整形1
b = 1.2  # 定义一个b变量，并赋值为整形1.2
c = "我爱中国"  # 定义一个c变量，并赋值为字符串"我爱中国"
e = True


class Person:
    pass


d = Person()  # 定义一个d变量，值为Person对象

print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)
print("e=", e)

print("========华丽分割线========")

a = 2  # 定义一个a变量，并赋值为整形1
b = 3.8  # 定义一个b变量，并赋值为整形1.2
c = "中国爱我"  # 定义一个c变量，并赋值为字符串"我爱中国"
e = False

print("a=", a)
print("b=", b)
print("c=", c)
print("e=", e)

#self training 
print("\n--------------self training-----------------")
var_demo_float = 12.42442
var_demo_int = 4242
var_demo_string = "i am a string!"
var_demo_bool = False#首字母大写


print (var_demo_int*var_demo_string)#整形乘以一个字符串是多个字符串
print(var_demo_int * var_demo_float)#整形乘以一个浮点数自动转化为浮点数
print(var_demo_float*var_demo_bool)#浮点数乘以bool是float

#多个不同类型打印用,隔开
print("varable float = ", var_demo_float, "," , "varable bool = ", var_demo_bool)

