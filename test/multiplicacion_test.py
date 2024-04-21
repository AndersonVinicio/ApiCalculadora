import unittest
import sys
sys.path.insert(0, '..')
from PYTHON.operaciones.multiplicacion.multiplicacion import multiplicacion

class TestMultiplicacion(unittest.TestCase):
    def test_multiplicacion(self):
        operacion = multiplicacion()
        self.assertEqual(operacion.multiplicacion(3, 2), 6)
        self.assertEqual(operacion.multiplicacion(2,3), 6)
        self.assertEqual(operacion.multiplicacion(-1, -1), 1)
        self.assertEqual(operacion.multiplicacion(2, 0), 0)
        self.assertEqual(operacion.multiplicacion(0, 2), 0)


if __name__ == '__main__':
    unittest.main()