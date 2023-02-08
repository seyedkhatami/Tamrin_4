import time

def timer(f):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        return f(*args, **kwargs)
    return wrapper

@timer
def k(z):
    for i in range(z):
        print(i)
k(13)