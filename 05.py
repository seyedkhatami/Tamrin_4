def function(z):
    def kwrapper(x, y):
        if y == 0:
            print("Cant divide by function")
            return
        return z(x, y)
    return kwrapper

@function
def func(a, b):
    print(a / b)
func(100, 2)