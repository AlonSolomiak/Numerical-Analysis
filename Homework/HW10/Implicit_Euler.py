import numpy as np

def Implicit_Euler(x0, y0, xf, delta, n):
    x = np.array([x0 + i * delta for i in range(int((xf - x0) / delta + 1))])
    y = np.array([0]*len(x), dtype=float)
    y[0] = y0

    for i in range(1, len(x)):
        y[i] = FPI(x[i], y[i-1], delta, n)
    
    return x, y


def f(x,y):
    return np.cos(y) + 5*x


def FPI(xi1: float, yi: float, delta, n: int) -> float:
    k = 1
    yk = yi
    yk1 = yi + f(xi1, yk) * delta
    while abs(yk1 - yk) > 10**-n:
        yk = yk1
        yk1 = yi + f(xi1, yk) * delta
        k += 1

    return yk1