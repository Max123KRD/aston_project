def add_func(a, b=2):
    return a + b


def mult_func(a, b=2):
    return a * b


def div_func(a, b):
    if b == 0:
        raise ValueError("Can not divide by zero")
    return a / b