import my_decorator

def decorator(func):
    def wrapper(*args, **kwargs):
        my_decorator.Entrance.append(*args, **kwargs)

        n = func(*args, **kwargs)
        my_decorator.output.append(n)
        return n
    return wrapper

@decorator
def f(name):
    return f"is {name}"

f("hello")
f("bye")

reslt1 = my_decorator.output
print(reslt1)

reslt2 = my_decorator.Entrance
print(reslt2)