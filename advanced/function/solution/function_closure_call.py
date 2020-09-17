def add(a, b):
    return a + b


def check(func):
    def wrapper(*args, **kwargs):
        print('hello')
    return wrapper


result = check(add)
del check
result()
# hello
