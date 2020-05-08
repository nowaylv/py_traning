print(" ============ list 操作 ============")
a = [1, 2, 3, 4]
print(len(a))  # 计算包含元素的个数
print(a[2])  # 获取集合第2个元素

# 修改第3个元素为5
a[3] = 5
print(a)

    
# 删除第3个元素
a.remove(a[3])
print(a)

# 向尾部添加一个元素
a.append(8)
print(a)

# 在第2个元素前插入一个元素7
a.insert(2, 7)
print(a)

# 将另一个集合添加到尾部
a.extend([0, 2, 5])
print(a)

# 查看元素7的索引
print(a.index(7))


# 排序
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 清空元素
a.clear()
print(a)

# self training
print("\n----------self training-------------")
list_demo = [1, 2, 3, 4, 4, 5, 4, 4, 4]
print(len(list_demo))


print(list_demo[-1:0:-3])

list_demo.append(2)
print(list_demo[:])

list_demo.insert(1, 90)
print(list_demo[:])

print(list_demo.index(4))

list_demo.remove(list_demo[1])

print(list_demo[:])

list_demo.sort()
print(list_demo[:])

print(list_demo.count(2) + list_demo.count(1))

print(list_demo[:])
list_demo_copy = list_demo.copy()#copy action haven't argument
#list_demo_copy = list_demo 也可以复制，但是相当于同一个列表不同的名字
print(list_demo_copy[:])
list_demo_copy[0] = 89
print(list_demo[0:1])

list_demo.pop(5)#pop's argument required indexs while remove's is list member

print(list_demo[:])
list_demo.clear()
print(list_demo[:])
