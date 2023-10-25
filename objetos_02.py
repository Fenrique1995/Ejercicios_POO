"""
Ejemplo: Clase para representar un Libro
Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se 
debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase 
e implementarla.
"""
class Libro:
    def __init__(self,titulo,autor,año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    def obtener_info(self):
        print(f'{self.titulo}\n{self.autor}\n{self.año}\n')


libro_uno = Libro('Rodan', 'Augusto', 1975)
#Asi puedo hacer uso del metodo obtener_info() que defini en Libro.
libro_uno.obtener_info()