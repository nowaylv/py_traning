print(" ============ set 操作 ============")
a = {9, 2, 3, 4}
print(len(a))  # 计算包含元素的个数

# set无顺序，所以和索引有关的操作都会报错
# print(a[2])
# print(a.index(4))

# 删除元素3
a.remove(3)
print(a)

# 添加元素5
a.add(5)
print(a)

# 添加元素2，因为set不能重复，set中有2，所以set没有变化
a.add(2)
print(a)

#self training 
print("\n--------------self training-----------------")
set_demo = {12,3,44,4,555,562,114312,4141234324,4121}
set_demo_copy = set_demo.copy()
print(len(set_demo))

set_demo.add(1)
print(set_demo)
print(set_demo_copy)

print(set_demo.difference(set_demo, set_demo_copy))

#set_demo.pop(set_demo[0])
set_demo.remove(3)#remove argument is value or set_demo[x]

print(set_demo)

'''
# 添加元素5
'''
