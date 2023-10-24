#TEMA 3: Estructuras condicionales anidadas
#PROBLEMAS PROPUESTOS
#DIEGO LEON GOVEA ORTIZ
import os

#Programa 1
nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
prom=(nota1+nota2+nota3)/3
if prom>=7:
    print("Promocionado")
else:
    if prom>=6:
        print("Regular")
    else:
        print("Reprobado")

#Programa 2
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

mayor = numero1

if numero2 > mayor:
    mayor = numero2

if numero3 > mayor:
    mayor = numero3

print("El número mayor es:", mayor)

#Una forma de hacerlo con python sin tener que pensar en la lógica es

numero_mayor = max(numero1, numero2, numero3)
print("El número mayor es:", numero_mayor)

#Programa 3

valor=int(input("Ingresa un numero real: "))

if valor>0: print("El numero es positivo")
elif valor <0: print("El numero es negativo")
elif valor==0: print("El valor es 0")

#Programa 4

print("Programa 4")
tres=int(input("Ingresa un numero entero de no màs de tres cifras: "))

if tres >= 0:
    if tres < 10: print("Es un numero de una cifra")
    elif tres <= 99: print("Es un numero de dos cifras")
    elif tres <= 999: print("Es un numero de tres cifras")
    else:
        print("Numero de màs de tres cifras o sea, invalido")
else:
    print("Numero negativo, por lo tanto es invalido")





