a = "hello"
b = "world"

# 字符串连接
c = a + " " + b
print(c)

print("=========================")

# 通过转义字符让字符串换行
d = a + "\n" + b
print(d)

print("=========================")
# 普通字符串和r字符串
print("hello\nworld")
print(r"hello\nworld")

print("=========================")
# 字符串切片操作
print(a[1:])

print("=========================")
# 查找字串llo
print(a.index("llo"))  # 如果不存在该字串会报错
print(a.find("llo"))  # 如果不存在该字串会返回-1

print("=========================")
# 格式化字符串
print("{} {}!".format(a, b))#{}空占位
print(f"{a} {b}!")

#self training 
print("\n--------------self training-----------------") 

demo_a = "12"
demo_b = "3s2 gfsd sgsg"
print(demo_a + " " + demo_b)#只有同类型才能用+拼接 ，不同类型用，

demo_c = demo_a + demo_b#可以拼接成另一个变量
demo_d = demo_a + "\n" + demo_b#拼接之后可以付给一个变量
print(demo_c)
print(demo_d)

print("gaagaad\r\n")
print(r"gadaga\r\n")

print(demo_a[1:])#字符串也可以切片

print(demo_b.index("2"))#索引不到将会编译错误
print(demo_b.find("1"))#找不到会返回-1

print("{},{}".format(demo_a , demo_b))
print(f"{demo_a} {demo_b} {demo_c}")