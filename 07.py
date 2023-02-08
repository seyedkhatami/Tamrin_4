import psutil

def timer(f):
    def wrapper(*args, **kwargs):
        n = psutil.virtual_memory()[4]
        res = f(*args, **kwargs)
        e = psutil.virtual_memory()[4]
        print(f"latency: {e - n}")
        return res
    return wrapper

@timer
def k(z):
    for i in range(z):
        pass
k(10000000)