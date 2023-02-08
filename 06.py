import time

def timer(f):
    def wrapper(*args, **kwargs):
        n = time.perf_counter()
        print(n)
        res = f(*args, **kwargs)
        e = time.perf_counter()
        print(e)
        print(f"new time : {e - n}")
        return res
    return wrapper

@timer
def k(z):
    for i in range(z):
        pass
k(13)