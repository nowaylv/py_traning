# 创建一个人类
class Person:

    def say(self, content):
        print(content)


# 实例化张三
zhang3 = Person()
zhang3.say("您好")

# 实例化李四
li4 = Person()
li4.say("新年好")

#self training 
print("\n--------------self training-----------------")
def hihi(fafa):
    print(fafa)

class action_demo:
    def display(self, lan, ty):
        print(lan)
        zhang3.say("hi")
        hihi(ty)

action = action_demo()

action.display("noway", "fafa")