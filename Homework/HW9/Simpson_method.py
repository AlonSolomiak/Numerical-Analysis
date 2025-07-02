import numpy as np

def Simpson_method(x: np.ndarray, y: np.ndarray):
    n = len(x)
    if n != len(y) or n < 3 or (n - 1) % 2 != 0:
        raise ValueError("x and y must have the same length, at least three points, and an odd number of points.")
    
    h = x[1] - x[0]
    integral = y[0] + y[n-1]

    for i in range(1, n-1, 2):
        integral += 4 * y[i]
    for i in range(2, n-2, 2):
        integral += 2 * y[i]

    integral *= h / 3

    return integral