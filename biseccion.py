#!/usr/bin/env python3
import math
def biseccion(f,a,b, error=None, h=10):
    # Comprobante formula
    if f(a) * f(b) >= 0:
        print("no se puede")
        return None
    # pasos utilizados
    if error is not None:
        h= math.ceil(math.log((b - a) / error) / math.log(2))
    # bissecion
    for n in range(h + 1):
        x = (a + b) / 2
        if f(x) == 0:
            return x
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return (a + b) / 2

if __name__ == '__main__':
    f = lambda x: x**2 + 2*x - 8
    print(biseccion(f,0,5,1e-2))