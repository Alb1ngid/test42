# классы ооп методы магичесике методы

types = 123,'str',True,1.1232,[],(),{}


# print(type(types))


def a(b,c):
    return b+c
d=11
l=11
a(l,d)

print(a(8,9))
print(a(88,99))

# 1 название с большой буквы
class Car:
    стекло=6
    колеса=4
    # магический метод-для использования стандартных функций
    def __init__(self,name,age,color): #конструктор класса
        self.name = name
        self.age = age
        self.color = color


    def __str__(self):
        return f'{self.name}, {self.age} , {self.color}'

    def __len__(self):
        return len(self.name)

    # свойства- переменная внутри класса
    # методы-функция внутри класса(def)

    def printCar(self):
        print(self.name,self.age,self.color)

# обьект\экземпляр класса

bmw=Car('bmw',2020,'black')
print(bmw)
bmw.printCar()
# printCar(bmw)
# bmw.printCar()

mersedes=Car('mersedes',2022,'red')
print(mersedes)
print(len(mersedes))