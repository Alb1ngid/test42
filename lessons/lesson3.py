# инкапсуляция
# git clone
# 4 наследование и полиморфизм
# инкапсуляция абстракция
# 1 способ создания класса и запись в него (наполнения внутренности )
# 2 уровни защиты внутренностей у класса их есть 3
# публичный
# 2 _protected : защищенный
# 3 __ скрытый
#
class Person:#родительский\супер класс
    _key=1234
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return (f'{self.name} is {self.age} years\n'
                f'{self._key} is key\n')

    def keys(self):
        print(self._key)


# b=1
# b=23
# print(b)

# p1=Person('beka',20)
# print(p1)
#
# p1.key='qwerty124'
#
# #
# p1.money=10000
# print(p1,p1.money)
# print(dir(p1))
#
# p1.key='0'
# print(p1)
# p2=Person('beka',21)
# print(p2)
#
# p3=Person('beka',30)
# print(p3)
class Person2(Person): #дочерний класс
    def __init__(self, name, age,money=0):
        super().__init__(name, age)
        self.__money = money

    def keys(self):
        print('money: ',self.__money)
        super().keys()

p1_1=Person2('beka',20,9000)
p1_1.__money = 100000000

# p1_1.keys()

class Person3(Person2):
    def __init__(self, name, age,money):
        super().__init__(name, age)
        self.__money=money
#     setter and getter
    def getmoney(self):
        print(self.__money)

    def setmoney(self,money1):
        self.__money=money1

    def keys(self):
        super().keys()
        print('money is class Person3: ',self.__money)



c1=Person3('beka',20,90)
c1.keys()
c1.setmoney(1000)


c1.keys()

print(dir(c1))
print(Person3.mro())
# git clone