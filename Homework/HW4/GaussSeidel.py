import numpy as np

def GaussSeidel(A: np.ndarray, b: np.ndarray, m: int) -> np.ndarray:
    n = len(A)
    x_i = np.array([0] * n, dtype=float)
    x_f = np.array([0] * n, dtype=float)
    
    while True:
        for i in range(n):
            x_i[i] = x_f[i]
        for i in range(n):
            sum1 = 0
            for j in range(i):
                sum1 += A[i][j] * x_f[j]
            sum2 = 0
            for j in range(i+1, n):
                sum2 += A[i][j] * x_i[j]

            x_f[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        if convergence_criterion(x_i, x_f, m):
            break

    return x_f
        

def convergence_criterion(x_i: np.ndarray, x_f: np.ndarray, m: int) -> bool:
    max_diff = max(abs(x_f[i] - x_i[i]) for i in range(1, len(x_i)))
    return max_diff < 10**-m