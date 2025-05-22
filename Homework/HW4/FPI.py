def FPI(x0, m, n):
    i = 0
    while convergence_criterion(x0, m, n):
        x0 = g(x0)
        i += 1

    return g(x0), i+1

def convergence_criterion(x0, m, n):
    if abs(x0 - g(x0)) < 10**-m and abs(f(x0)) < 10**-n:
        return False
    return True

def f(x: float) -> float:
    return x**3 + 2*x + 2

def g(x: float) -> float:
    return -(x**3)/5 + (3/5)*x - 2/5