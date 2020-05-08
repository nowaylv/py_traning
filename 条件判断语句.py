a = False

if a:
    print("当前 a = True")
else:
    print("当前 a = False") 

print("============================")

b = 1
if b == 0:
    print("当前 b = 0")
elif b == 1:
    print("当前 b = 1")
else:
    print("当前 b = 其它")


#self training 
print("\n--------------self training-----------------")
judge_demo = "noway"
judge_float = 4.242

if judge_demo == "noway":#可以判别字符串
    print("judge string is successed")

else:
    print("judge string is loose")

if judge_float == 4.242:
    print("judge float ok")
else:
    print("judge float fall")

