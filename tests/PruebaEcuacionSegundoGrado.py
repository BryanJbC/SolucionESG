import math
import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado


class PruebaEcuacionSegundoGrado(unittest.TestCase):

    def test_EcuacionSegundoGrado_parametrosNumericos_RaicesReales(self):
        #arrange
        a=3
        b=-5
        c=1
        x1Esperado = 1.43
        x2Esperado = 0.23

        #do
        ecuacion = EcuacionSegundoGrado()
        x1Actual, x2Actual = ecuacion.calculoESG(a,b,c)


        #Asert
        precision = math.fabs(x1Esperado - x1Actual)
        self.assertLessEqual(precision,0.01)
        precision = math.fabs(x2Esperado - x2Actual)
        self.assertLessEqual(precision,0.01)

    def test_EcuacionSegundoGrado_parametrosNumeriosMultiples_raicesReales(self):
        #arrange
        ecuacion = EcuacionSegundoGrado()
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperado1": 1.43, "RaizEsperado2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperado1": -1.00, "RaizEsperado2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperado1": 1.00, "RaizEsperado2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperado1": 4.24, "RaizEsperado2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperado1": 0.00, "RaizEsperado2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperado1": -2.00, "RaizEsperado2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperado1": -1.00, "RaizEsperado2": -2.00},

        )
        #do
        for item in items:
            with self.subTest(item["Case"]):
                RaizActual1, RaizActual2 =ecuacion.calculoESG(item["a"],item["b"],item["c"])

        #Asert


        precision = math.fabs(item["RaizEsperado1"]-RaizActual1)
        self.assertLessEqual(precision,0.01)
        precision = math.fabs(item["RaizEsperado2"] - RaizActual2)
        self.assertLessEqual(precision, 0.01)



