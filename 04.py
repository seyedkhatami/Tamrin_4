import functools

def cache(n):
    cache.my_cache = {}

    functools.wraps(n)
    def wrapper(*args):
        key = ", ".join([str(item) for item in args])

        res = cache.my_cache.get(key)
        if not res:
            res = n(*args)
            cache.my_cache[key] = res
        return res
    return wrapper

@cache
def f(s):
    if s < 2:
        return 1
    return f(s - 3) + f(s - 6)
print(f(4))
