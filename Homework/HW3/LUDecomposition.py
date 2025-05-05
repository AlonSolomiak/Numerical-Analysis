from typing import Tuple
import numpy as np


def LUDecomposition(A: np.ndarray,b: np.ndarray) -> np.ndarray:
    ValidateInput(b, A)
    (P, L, U) = GetLU(A)
    Pb = MatrixVectorMultiply(P, b)
    y = SolveLyb(L, Pb)
    x = SolveUxy(U, y)

    return x


def GetLU(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    n, L, U, P = InitializeLUP(A)

    for i in range(n):
        max_row, max_val = FindMaxRow(U, i)

        if max_val == 0:
            raise ValueError("Matrix is singular")

        if max_row != i:
            SwapRows(U, i, max_row)
            SwapRows(P, i, max_row)

            # Swap rows in L (columns before i only) 
            for j in range(i):
                temp = L[i][j]
                L[i][j] = L[max_row][j]
                L[max_row][j] = temp

        # Elimination
        for j in range(i+1, n):
            L[j][i] = U[j][i] / U[i][i]
            for col in range(i, n):
                U[j][col] = U[j][col] - L[j][i] * U[i][col]

    return P, L, U


def InitializeLUP(A: np.ndarray) -> Tuple[int, np.ndarray, np.ndarray, np.ndarray]:
    n = A.shape[0]
    L = np.array([[0]*n]*n, dtype=float)
    U = np.array([[0]*n]*n, dtype=float)
    P = np.array([[0]*n]*n)

    # Initialize L and P as identity matrices
    for i in range(n):
        L[i, i] = 1
        P[i, i] = 1

    # Copy A to U
    for i in range(n):
        for j in range(n):
            U[i][j] = A[i][j]

    return (n, L, U, P)


def FindMaxRow(U: np.ndarray, i: int) -> Tuple[int, float]:
    max_row = i
    max_val = abs(U[i][i])
    for row in range(i + 1, U.shape[0]):
        if abs(U[row][i]) > max_val: # Because we are looking for the largest ABSOLUTE value
            max_val = abs(U[row][i])
            max_row = row

    return (max_row, max_val)


def SwapRows(A: np.ndarray, i: int, j: int) -> None:
    A[i] += A[j]
    A[j] = A[i] - A[j]
    A[i] -= A[j]



def SolveLyb(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = L.shape[0]
    y = np.array([0]*n, dtype=float)
    
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i, j] * y[j]
        y[i] = b[i] - sum
    
    return y


def SolveUxy(U: np.ndarray, y: np.ndarray) -> np.ndarray:
    n = U.shape[0]
    x = np.array([0]*n, dtype=float)
    
    for i in range(n):
        sum = 0
        for col in range(n-i, n):
            sum += U[n-1-i, col] * x[col]
        x[n-1-i] = (y[n-1-i] - sum) / U[n-1-i, n-1-i]
    
    return x


def MatrixVectorMultiply(A: np.ndarray, v: np.ndarray) -> np.ndarray:
    result = np.array([0]*A.shape[1], dtype=float)
    
    for matrix_col in range(A.shape[1]):
        for matrix_row in range(A.shape[0]):
            result[matrix_col] += A[matrix_row,matrix_col] * v[matrix_row]
    
    return result


def ValidateInput(v: np.ndarray, A: np.ndarray) -> None:
    if len(v.shape) != 1 or len(A.shape) != 2:
        raise ValueError("Input should be a vector and a matrix")
    if v.shape[0] != A.shape[0]:
        raise ValueError("The vector's length does not match the matrix' width")