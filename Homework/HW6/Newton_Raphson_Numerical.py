import numpy as np

def Newton_Raphson_Numerical(x0: np.ndarray,m,n,inc):
    if len(x0) != 2:
        raise ValueError("x0 must be a 2-dimensional vector.")

    x = np.array(x0, dtype=float)
    i = 1
    J = Numerical_Jaacobian(x, inc)
    f_x = f(x)
    delt = delta(J, f_x)

    for i in range(len(f_x)):
        x[i] += delt[i]

    while norm(delt) > 10**-m and norm(f_x) > 10**-n:
        print(x)
        J = Numerical_Jaacobian(x, inc)
        f_x = f(x)
        delt = delta(J, f_x)
        for i in range(len(f_x)):
            x[i] += delt[i]
        i += 1

    return x, i

def f(x: np.ndarray) -> np.ndarray:
    return np.array([40*x[0]**4 + 8*x[0]*x[1] - 16*x[1] - 32, 4*x[0]**2 - 16*x[0] + 8*x[1]])


def Numerical_Jaacobian(x: np.ndarray, incr) -> np.ndarray:
    n = len(x)
    J = np.array([[0]*n]*n, dtype=float)
    f_x = f(x)

    for i in range(n):
        x_i = np.array(x, dtype=float)
        x_i[i] += incr
        f_x_i = f(x_i)
        J[:, i] = (f_x_i - f_x) / incr
    
    return J

def delta(J: np.ndarray, f_x: np.ndarray) -> np.ndarray:
    delta = np.array([0] * len(f_x), dtype=float)

    for i in range(len(f_x)):
        det = determinant(J)
        if det == 0:
            raise ValueError("Jacobian determinant is zero, cannot proceed with Newton-Raphson method.")
        J_temp = np.array(J, dtype=float)
        J_temp[:, i] = -f_x
        delta[i] = determinant(J_temp) / det

    return delta

def determinant(A: np.ndarray) -> float: # for 2 by 2 matrix
    if A.shape[0] != 2 or A.shape[1] != 2:
        raise ValueError("Matrix must be 2x2 for this function.")
    return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

def norm(x: np.ndarray) -> float:
    norm = 0
    for i in range(len(x)):
        norm += x[i] ** 2
    return norm ** 0.5