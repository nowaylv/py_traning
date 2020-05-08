# 循环不会打印出5
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")

print("\n=======================")
#循环不会打印出5后面的数
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

#self training 
print("\n--------------self training-----------------")

for num in range(3, 10, 2):#可以有3个参数，start , stop, step，和切片类似
    if num == 5:
        continue
    print(num, end=" ")#类型html