
import sys
sys.path.insert(0, '..')
from PYTHON.operaciones.resta.resta import resta
from PYTHON.operaciones.suma.suma import suma
from PYTHON.operaciones.multiplicacion.multiplicacion import multiplicacion
from PYTHON.operaciones.division.division import division


def main():
    claseSuma = suma()
    claseResta = resta()
    claseMultiplicacion = multiplicacion()
    claseDivision = division()

if  __name__ == "__main__":

    main()