#Escribir una función que calcule el máximo común divisor entre dos números
#mcd es el n° mas grande que divide dos numeros
'''
con la funcion math de python
import math
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
print(math.gcd(num1,num2))
print(math.gcd(4,8))'''


def mcd(x,y):
    mcd = 1

    if x % y == 0:
        return y
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mdc=k
            break
    return mcd
print(mcd(8,4))
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese el segundo numero: "))
print(mcd(num1,num2))


