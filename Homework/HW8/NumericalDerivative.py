import numpy as np

def NumericalDerivative(x: np.ndarray,f: np.ndarray):
    n = len(x)
    if n != len(f):
        raise ValueError("x and f must have the same length")
    
    df = np.array([0]*n, dtype=float)
    ddf = np.array([0]*n, dtype=float)


    return df, ddf