import math
class EcuacionSegundoGrado:
    def calculoESG(self, a,b,c):
        discriminante = math.pow(b,2) - 4 * a * c
        if discriminante >= 0:
            raizdiscriminante = math.sqrt(discriminante)
            x1= (-b + raizdiscriminante)/ (2*a)
            x2 = (-b - raizdiscriminante) / (2*a)
            return x1,x2

