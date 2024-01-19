import numpy as np

def add_numbers(a, b):
    return np.array(a + b)

def multiply_numbers(a, b):
    return np.array(a * b)

def subtract_numbers(a, b):
    return np.array(a - b)

def divide_numbers(a, b):
    if b == 0:
        raise ValueError
    return np.array(a / b)
