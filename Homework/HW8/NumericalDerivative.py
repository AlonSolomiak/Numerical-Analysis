import numpy as np

def NumericalDerivative(x: np.ndarray,f: np.ndarray):
    n = len(x)
    if n != len(f) or n < 3:
        raise ValueError("x and f must have the same length and at least three points.")
    
    dx = abs(x[1] - x[0])  # Assuming uniform spacing for simplicity
    df = np.array([0]*n, dtype=float)
    ddf = np.array([0]*n, dtype=float)

    # Forward differences for the first point
    df[0] = (f[1] - f[0]) / dx 
    ddf[0] = (f[2] - 2*f[1] + f[0]) / (dx**2)

    # Central differences for the first and second derivatives
    for i in range(1, n-1):
        df[i] = (f[i+1] - f[i-1]) / (2 * dx) 
        ddf[i] = (f[i+1] - 2*f[i] + f[i-1]) / (dx**2)

    # Backward difference for the last point
    df[n-1] = (f[n-1] - f[n-2]) / dx
    ddf[n-1] = (f[n-1] - 2*f[n-2] + f[n-3]) / (dx**2)

    return df, ddf