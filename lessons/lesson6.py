# декораторы
import time
p={1:'12w'}
def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end = time.time()
        print(f'время выполнения функции {func.__name__}: {end - start} секунд')
        return result
    return wrapper


@timeit
def my_function(n):
    total =0
    for i in range(n):
        i=i*2
        total+= i
    return total


print(my_function(100000))
print(my_function(10000000000))