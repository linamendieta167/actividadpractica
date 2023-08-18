#MCM es el numero positivo mas pequeño que es multiplo de dos numeros

def mcm(x,y):
    z = max(x,y)
    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        z += 1
print(mcm(2,4))
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
print(mcm(num1,num2))
