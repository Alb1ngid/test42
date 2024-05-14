

class MyClass:
    def __init__(self,value,vel2):
        self._value = value
        self._vel2 = vel2
    def get_value(self):
        print(self._value,self._vel2)
        return self._value

    def set_value(self,new_value,new3):
        self._value = new_value
        self._vel2 = new3
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value):
        self._value = new_value
    @value.deleter
    def value(self):
        del self._value


obj1 = MyClass(10,19)

# obj1.get_value()
# obj1.set_value(20,18)
# obj1.get_value()
print(obj1.value)
obj1.value=20
print(obj1.value)
del obj1.value
obj1.value=21
obj1.get_value()

