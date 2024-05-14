#множественное наследование
# 1 принцип ооп наследование
# mro - method resolution order
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def res(self):
        print(self.name,self.age)


class B:
    def __init__(self,name,age,b):
        self.name = name
        self.age = age
        self.b=b
    def res(self):
        print('эта функция класса B')

class C(A,B):
    pass
    # def res(self):
    #   ...

c=C('name',21)


# print(dir(c))





if __name__ == '__main__':
    A.res(c)
    print(C.mro())


