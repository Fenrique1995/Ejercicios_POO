"""
Ejemplo: Clase para representar un Rectángulo
Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe 
poder calcular el área y el perímetro. Se debe crear la clase e implementarla.
"""
class Rectangulo:
    def __init__(self,base,altura):
        self.base = int(base)
        self.altura = int(altura)

    def perimetro(self):
        perimetro_rectangulo = 2 * self.base + 2 * self.altura

        print(perimetro_rectangulo)

recatangulo_uno = Rectangulo("5",3)
recatangulo_uno.perimetro()
#Hice lo mismo que con el de Libro solo que verifique que sean enteros los parametros