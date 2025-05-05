from typing import Tuple
import numpy as np

def LUDecomposition(A: np.ndarray,b: np.ndarray) -> np.ndarray:
    (L, U) = GetLU(A)
    print(L)
    print(U)
    y = SolveLyb(L, b)
    print(y)
    x = SolveUxy(U, y)
    print(x)

    return x

def GetLU(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    n = A.shape[0]
    L = np.array([[0]*n]*n)
    U = A

    for i in range(n):
        L[i, i] = 1
    
    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += L[i, j] * U[j, k]
            U[i, k] = A[i, k] - sum
        for k in range(i+1, n):
            sum = 0
            for j in range(i):
                sum += L[k, j] * U[j, i]
            L[k, i] = (A[k, i] - sum) / U[i, i]
    
    return L, U

def SolveLyb(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = L.shape[0]
    y = np.array([0]*n)
    
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i, j] * y[j]
        y[i] = b[i] - sum
    
    return y

def SolveUxy(U: np.ndarray, y: np.ndarray) -> np.ndarray:
    n = U.shape[0]
    x = np.array([0]*n)
    
    for i in range(n):
        sum = 0
        for j in range(n-1-i+1, n):
            sum += U[n-1-i, j] * x[j]
        if U[n-1-i, n-1-i] != 0:    
            x[n-1-i] = (y[n-1-i] - sum) / U[n-1-i, n-1-i]
        else:
            x[n-1-i] = (y[n-1-i] - sum)
    
    return x