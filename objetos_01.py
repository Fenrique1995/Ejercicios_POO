"""
Ejemplo: Clase simple
Crear una clase Persona que tenga las características nombre y edad. La persona debe poder 
mostrar un mensaje saludando presentándose con su nombre y edad. Se debe crear la clase e 
implementarla.
"""
#Se declara la clase/objeto Persona 
class Persona:
    #Aca se definen los atributos de la clase/objeto Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Aca se define un metodo de tipo __str__ el cual devuelve un str
    def __str__(self):
        return f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años.'

#Declaro un objeto que es persona uno y le doy los atributos de:
                    #NOMBRE  Y  EDAD.
persona_uno = Persona('Jhonatan', 25)
#Printeo y me devuelve el str de la persona presentandose con nombre y edad.
print(persona_uno)