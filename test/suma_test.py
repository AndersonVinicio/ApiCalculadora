import unittest
import sys
sys.path.insert(0, '..')
from PYTHON.operaciones.suma.suma import suma

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        operacion = suma()
        self.assertEqual(operacion.sumar(3, 2), 5)
        self.assertEqual(operacion.sumar(-1, 1), 0)
        self.assertEqual(operacion.sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()