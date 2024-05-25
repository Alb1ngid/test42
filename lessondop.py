#1 урок
print()
# len()
# abs()
class A:
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def andd(self):
        print('это метод класса А')

a=A('17',
    'beka')
A.andd(a)
a.andd()

