class Person:

    def __call__(self):
        print("调用__call__行为")

zhang3 = Person()
zhang3()

#self training
class noway:
    def __call__(self):
        print("noway")


n = noway()
n()