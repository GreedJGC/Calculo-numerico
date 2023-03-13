#!/usr/bin/env python3
import unittest
import errores
import integracion_numerica
import teorema
import biseccion
import newton

class test_errores(unittest.TestCase):
    def test_error_absoluto(self):
        self.assertEqual(errores.Error_absoluto(5,4),1)
        self.assertEqual(errores.Error_absoluto(20000,19999),1)

    def test_error_relativada(self):
        self.assertEqual(errores.Error_relativo(5,4),0.2)
        self.assertEqual(errores.Error_relativo(20000,19999),5e-05)

class test_teoremas(unittest.TestCase):
    def test_valor_intermedio(self):
        f= lambda x :x**2-4
        self.asserTrue(teorema.Valor_intermedio(f,0,5),True)

class test_biseccion(unittest.TestCase):
    def test_biseccion(self):
        f=lambda x:x**2+2*x-8
        self.asssertEqual(biseccion.biseccion(f,0,5,1e-2),1.99951171875)

class test_integracion_numerica(unittest.TestCase):
    def test_integracion_numerica(self):
        f=lambda x:x**2
        self.assertEqual(integracion_numerica.integracion(f,0,1,10),0.3850000000000001)

class test_newton(unittest.TestCase):
    def test_newton(self):
        f=lambda x:x**2+2*x-8
        der = lambda x: 2*x + 2
        self.assertEqual(newton.newton(f,der,10,m=10),2.0000001002152237)

if __name__ == "__main__":
    unittest.main()
