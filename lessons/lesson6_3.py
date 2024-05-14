import time

def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end = time.time()
        print(f'время выполнения функции {func.__name__}: {end - start} секунд')
        return result
    return wrapper

class Timeit:
    def __init__(self,func='q'):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()  # Запоминаем время начала выполнения функции
        result = self.func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Запоминаем время окончания выполнения функции
        print(f"Время выполнения функции {self.func.__name__}: {end_time - start_time} секунд")
        return result
class MyClass:
    def __init__(self, value):
        self._value = value

    @Timeit
    def get_value(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    @Timeit
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    @Timeit
    def value(self):
        del self._value



obj = MyClass(10)
print(obj.get_value())