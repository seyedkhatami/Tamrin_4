my_list = []

def function(func):
    def wrapper(*args, **kwargs):
        global my_list
        my_list.append(func.__name__)
        print(my_list)
        return func(*args, **kwargs)
    return wrapper

@function
def f():
    pass
f()

@function
def k():
    pass
k()

@function
def n():
    pass
n()

@function
def a():
    pass
a()