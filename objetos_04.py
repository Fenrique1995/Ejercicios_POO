"""
Ejemplo: Clase para representar una Calculadora
Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. Se debe 
crear la clase e implementarla.
"""
class Calculadora:
    def __init__(self, operacion, numero1, numero2):
        self.operacion = operacion
        self.numero1 = int(numero1)
        self.numero2 = int(numero2)
        self.operaciones =["sumar", "restar", "multiplicación", "division"]

    def calculo(self):
        if self.operacion not in self.operaciones:
            print('ERROR 404')
        elif self.operacion == "sumar":
            resultado = self.numero1+self.numero2
            print(str(resultado))
        elif self.operacion == "restar":
            resultado = self.numero1-self.numero2
            print(str(resultado))
        elif self.operacion == "multiplicación":
            resultado = self.numero1*self.numero2
            print(str(resultado))
        elif  self.operacion == "division":
            if self.numero2 > 0:
                resultado = self.numero1/self.numero2
                print(str(resultado))
            else:
                print('ERROR 202')

calculadora_uno = Calculadora('division',2,1)
calculadora_uno.calculo()