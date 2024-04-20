import unittest
import sys
sys.path.insert(0, '..')
from PYTHON.operaciones.resta.resta import resta

class TestResta(unittest.TestCase):
    def test_sumar(self):
        operacion = resta()
        self.assertEqual(operacion.resta(3, 2), 1)
        self.assertEqual(operacion.resta(2,3), -1)
        self.assertEqual(operacion.resta(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()