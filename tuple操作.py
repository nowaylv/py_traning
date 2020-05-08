print(" ============ tuple 操作 ============")
a = (1, 2, 3, 4)
print(len(a))  # 计算包含元素的个数
print(a[2])  # 获取集合第2个元素

# 查看元素4的索引
print(a.index(4))

# tuple不能修改，所以任何修改性操作都会报错
#a[2]=5

#self training 
print("\n----------self training-------------")
tuple_demo = (2,34,4434,4442,33,3,11,1,11,1111,111111111)

print(tuple_demo)
print(tuple_demo.count(1))
print(len(tuple_demo))
print(tuple_demo.index(1111))