import numpy as np

def Lagrange_poly(X: np.ndarray, k: int, x_eval: float) -> float:
    n = len(X)

    lk = 1
    for i in range(n):
        if i != k:
            lk *= (x_eval - X[i])

    return lk