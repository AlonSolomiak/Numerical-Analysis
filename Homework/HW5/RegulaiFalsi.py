def f(x):
    raise NotImplementedError

def RegulaiFalsi(XL, XR, n):
    x = XL - (f(XL) * (XR - XL)) / (f(XR) - f(XL))
    i = 0

    while abs(f(x)) > 10**-n:
        if f(XL) * f(x) < 0:
            XR = x
        else:
            XL = x
        x_new = XL - (f(XL) * (XR - XL)) / (f(XR) - f(XL))
        i += 1
        if abs(x_new - x) < 10**-n:
            break
        x = x_new


    return x, i