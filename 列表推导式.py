a_list = [1, 2, 3, 4, 5, 6]
b_list = []
for a in a_list:
    b_list.append(a * 2)
print(b_list)

# 将上面的代码简化为下面代码
c_list = [x * 2 for x in a_list]
print(c_list)

#self training 
print("\n--------------self training-----------------")
list_demo_a = [1,22, 2, 2, 3, 4,5,5,5]
list_demo_b = []

for x in list_demo_a:
    list_demo_b.append(x)

print(list_demo_b)#use table and ':' to divide code block