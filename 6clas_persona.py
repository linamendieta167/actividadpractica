'''Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.'''

class Persona():
    def __init__(self,nombre=None,edad=None,dni=None):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
        
        #getter(obtener metodo get)  
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_dni(self):
        return self.__dni
    
    #setter (modificar metodo set)
    
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_edad(self,edad):
        self.__edad = edad
        
def set_dni(self, dni):
        if dni.isdigit() and len(dni) == 8:  # Validar que el DNI sea numérico y tenga 8 dígitos
            self.__dni = dni
        else:
            print("Error: DNI inválido")


def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

def mayor_edad(self):
        return self.__edad >= 18

nombre = input("ingrese nombre:")
edad = int(input("ingrese edad: "))
dni: input("ingrese dni:")

persona = Persona(nombre, edad, dni)

persona.mostrar()

if persona.mayor_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")