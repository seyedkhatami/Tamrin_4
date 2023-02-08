def genrat(operate):
    def kwrapper(x, y):
        if y == 0:
            print("Can't divide by genrat")
            return
        return operate(x, y)
    return kwrapper

@genrat
def division(a, b):
    print(a/b)

division(50, 0)
