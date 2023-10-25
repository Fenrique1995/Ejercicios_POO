'''
Ejemplo: Encapsulamiento
Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. De la 
cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue
exitoso). Se debe crear la clase e implementarla
'''
# el .__ hace que sean privados de verdad (existe ._ pero es mas superficial)
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = float(saldo) 

    def obtener_titular(self):
        return self.__titular

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        float(cantidad)
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad no válida para depósito.")

    def retirar(self, cantidad):
        float(cantidad)
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad no válida para retiro o saldo insuficiente.")

cuenta = CuentaBancaria("Juan Pérez", 1000.0)

#print(cuenta.__titular) Esto seria un error, al estar el atributo encapsulado no se podra acceder a el desde afuera 
print(cuenta.obtener_titular()) #Aqui si se podria acceder al titular
print(cuenta.obtener_saldo())
#Y usar los metodos
cuenta.depositar(2000)
#Queda mas que claro que si se modifico el saldo
print(cuenta.obtener_saldo())