#!/usr/bin/env python3
def newton(f, der, x, eps=1e-6, m=50):   
    for n in range(m + 1):
        # Evaluación de la función para ver si el resultado es válido
        f_x = f(x)
        if abs(f_x) < eps:
            return x
        # Evaluación de la derivada
        d_f = der(x)
        if d_f == 0:
            print('Error la derivada es cero')
            return None
        # Estimación del siguiente punto
        x-= f_x / d_f
    print('Se ha alcanzado el límite de iteraciones')
    return None

if __name__ == '__main__':
    f = lambda x: x**2 + 2*x - 8
    der = lambda x: 2*x + 2#derivada de f
    print(newton(f, der, 10, m=10)) 
