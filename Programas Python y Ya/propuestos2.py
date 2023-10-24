#TEMA 2: Estructuras condicionales simples y compuestas
#PROBLEMAS PROPUESTOS
#DIEGO LEON GOVEA ORTIZ
import os

#Programa 1
print("Programa 1")
sueldo=int(input("Ingrese cual es su sueldo:"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")
os.system("pause")


#Programa 2
print("Programa 2")
num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)
os.system ("pause")


#Programa 3
print("Programa 3")
numI=int(input("Ingrese primer valor:"))
numII=int(input("ingrese segundo valor:"))
sumI=numI+numII
res=numI-numII
pro=numI*numII
div=numII/numI
if num1>num2:
    print("El primero es el mayor")
    print("Su suma es -> ",sumI)
    print("Su diferencia es -> ",res)
else:
    print("El segundo es el mayor")
    print("Su producto es -> ", pro)
    print("Su division es -> ", div)
os.system ("pause")

#Programa 4: Aprobado y Reprobado
print("Programa 4")
print("Ingresa 3 calificaciones:")
calI=float(input("Calificacion 1:"))
calII=float(input("Calificacion 2:"))
calIII=float(input("Calificacion 3:"))

promedio=(calI+calII+calIII)/3

print("La calificacion aprobatoria es 7")
print("Tu promedio es ",promedio)

if promedio>=7:
    print("APROBADO")
else:
    print("REPROBADO")

#Programa 5: Dos digitos
print("Programa 5")
num=int(input("Ingrese un numero del 1 al 99:"))
if num>=10:
    print("El numero tiene dos digitos")
else:
    print("El numero tiene un digito")



