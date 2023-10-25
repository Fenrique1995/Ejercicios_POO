'''
Ejemplo: Herencia de clases
Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal 
las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las 
características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que 
realizan. Se debe crear la clase e implementarla.
'''
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    #Aca por ejemplo cambie de lugar la funcion ladrar y ahora tanto perro como gato podrian acceder a ella pero lo hice como ejemplo simplemente
    def ladrar(self):
        print('guau guau')
#Tanto Perro como Gato heredan los atributos de Animal
class Perro(Animal):
    #Asi es como heredan los atributos el super() es la funcion que permite acceder a los atributos como los metodos si los tubiera 
    def __init__(self, nombre):
        super().__init__(nombre)
    '''
    def ladrar(self):
        print('guau guau')
    '''

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def maullar(self):
        print('Miau')

nombre_animal = Animal('LILO')
print(nombre_animal.nombre)

perro_uno = Perro('Bobby')
print(perro_uno.nombre)
perro_uno.ladrar()

gato_uno = Gato('Roy')
print(gato_uno.nombre)
gato_uno.maullar()