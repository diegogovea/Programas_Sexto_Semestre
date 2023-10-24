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
