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

        self.assertEqual(x1Esperado, x1Actual)
        self.assertEqual(x2Esperado, x2Actual,)


