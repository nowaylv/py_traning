print(" ============ dict 操作 ============")
a = {"name": "zhang3", "sex": "男", "age": 36}
print(len(a))
print(a["name"])

# 修改年龄
a["age"] = 37
print(a)

# 添加升高为1.72
a["height"] = 1.72
print(a)

# 删除性别属性
a.pop("sex")
print(a)

# self training
print("\n----------self training-------------")
noway_demo = {"height":"184cm", "weight":"64kg", "sex":"male", "sex":"male"}
print(len(noway_demo))
print(noway_demo["sex"])
noway_demo["weight"] = 150
print(noway_demo["weight"])

noway_demo.pop("sex")
print(len(noway_demo))

print(noway_demo.get("height"))

noway_demo.setdefault("ok")#like insert key, and key value is None, return the value of key or default

print(noway_demo.values())#return all value of keys
print(noway_demo)

#fromkeys用于创建新的字典每个键的值都是None
fasda  = noway_demo.fromkeys(["nanan", "fasfaf"])
#也可以自己提供默认值
value_user = noway_demo.fromkeys(["hhhh", "fafa"], "jijijij")
#也可以用空字典构造
demo_fromk = {}.fromkeys(["default", "name"], "noway")
print(demo_fromk)
print(value_user)
print(fasda)
print(noway_demo["height"])

#items会返回一个清单，但次序不一定一样
print(noway_demo.items())

#会随机弹出一项
noway_demo.popitem()
print(noway_demo)

#update会用一个字典更新您外一个字典的一项,旧字典没有的项会新增
u = {"fa": "faafffff"}
c = {"name": "zhang3", "sex": "男", "age": 36, "fa":"fafaaaaaa"}
u.update(c)
print(u)
