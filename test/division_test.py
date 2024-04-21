import unittest
import sys
sys.path.insert(0, '..')
from PYTHON.operaciones.division.division import division

class TestDivision(unittest.TestCase):
    def test_division(self):
        operacion = division()
        self.assertEqual(operacion.division(3, 2), "1.50")
        self.assertEqual(operacion.division(2,3), "0.67")
        self.assertEqual(operacion.division(-1, -1), "1.00")
        #EN ESTE CASO EN EL METODO DIVISION NO ARROJA LA EXCEPCION SI NO UN MENSAJE DE NO SE PUEDE DIVIDIR POR 0
        self.assertEqual(operacion.division(10, 0),"no se puede dividir por 0")
        self.assertEqual(operacion.division(0, 10),"no se puede dividir por 0")
        # CUANDO UN NUMERO ES DIVIDIDO POR 0 ARROJA UNA EXCEPCION ZeroDivisionError
        # with self.assertRaises(ZeroDivisionError):
        #     operacion.division(2, 0)
        #     operacion.division(0, 2)


if __name__ == '__main__':
    unittest.main()