import numpy as np

def Lagrange_interp(X: np.ndarray, F: np.ndarray, x_eval: float) -> float:
    if len(X) != len(F):
        raise ValueError("X and F must have the same length.")

    n = len(X)
    result = 0.0

    for k in range(n):
        result += F[k] * Lagrange_poly(X, k, x_eval) / Lagrange_poly(X, k, X[k])

    return result

def Lagrange_poly(X: np.ndarray, k: int, x_eval: float) -> float:
    n = len(X)

    lk = 1
    for i in range(n):
        if i != k:
            lk *= (x_eval - X[i])

    return lk