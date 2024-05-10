#venv пакеты библеотеки фреймворки

# модули зависимости


import random
num=[1,2,3,4,5]
# print(random.choice(num))
# библиотека
# 1 модуль - встроенный
import math
# print(math.e)
# print(math.pi)

from math import e,pi,cos,sin
from math import isfinite as fine
# print(e)
# print(fine(8))
# 2 вид - ваши\собвственные модули
from lesson4 import C


p=C('lesson5',1)
p.res()


# 3 вид модулей - внешние модули
import colorama
from art import tprint
print(colorama.Back.LIGHTGREEN_EX,colorama.Fore.BLACK)
tprint('hello world')

