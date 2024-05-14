import time

class CalculateTime:
    def __init__(self, func):
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

    @CalculateTime
    def get_value(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    @CalculateTime
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    @CalculateTime
    def value(self):
        del self._value

# Пример использования:
obj = MyClass(10)
print(obj.get_value())  # Вызываем метод, обернутый декоратором CalculateTime
obj.value = 20  # Устанавливаем новое значение, также замеряем время выполнения
del obj.value  # Удаляем значение с замером времени