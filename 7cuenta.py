class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("DNI del titular:", self.titular.dni)
        print("Cantidad:", self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


nombre_titular = input("Ingresar nombre del titular: ")
dni_titular = input("Ingresar DNI del titular: ")


titular = Persona(nombre_titular, dni_titular)

cuenta = Cuenta(titular)


cuenta.mostrar()

cantidad_ingreso_str = input("Ingrese la cantidad a ingresar (opcional): ")
if cantidad_ingreso_str:
    cantidad_ingreso = float(cantidad_ingreso_str)
    cuenta.ingresar(cantidad_ingreso)

cantidad_retiro_str = input("Ingrese la cantidad a retirar (opcional): ")
if cantidad_retiro_str:
    cantidad_retiro = float(cantidad_retiro_str)
    cuenta.retirar(cantidad_retiro)

cuenta.mostrar()