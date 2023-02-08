def decorator(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1

        print(f"The number of times it has been executed = {count}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def f():
    print("Hello")

f()
f()
f()
f()
f()