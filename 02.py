my_list = []

def over(func):
    def wrapper(*args, **kwargs):
        global my_list
        my_list.append(func.__name__)
        print(my_list)
        return func(*args, **kwargs)
    return wrapper

@over
def n():
    pass
n()

@over
def k():
    pass
k()

@over
def q():
    pass
q()
