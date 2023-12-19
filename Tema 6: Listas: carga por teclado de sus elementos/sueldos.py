#TEMA 6: Procesar cadenas de caracteres
#PROBLEMAS PROPUESTOS
#DIEGO LEON GOVEA ORTIZ

#Programa 1: Sueldos

#definimos una lista vacia
lista=[]
#definimos variable para acumular sueldos
acumulador=0
#disponemos un ciclo de 5 vueltas
for x in range(5):
    valor = float(input("Ingrese un sueldo:"))
    lista.append(valor)
    acumulador=acumulador+valor

promedio=acumulador/len(lista)
#imprimimos la lista
print(lista)
#imprimimos el promedio
print(promedio)
