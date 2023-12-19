#TEMA 6: Procesar cadenas de caracteres
#PROBLEMAS PROPUESTOS
#DIEGO LEON GOVEA ORTIZ

#Programa 2: Estaturas

#definimos una lista vacia
lista=[]
#definimos variable para acumular
acumulador=0
#disponemos un ciclo de 5 vueltas
for x in range(5):
    valor = float(input("Ingrese un estatura:"))
    lista.append(valor)
    acumulador=acumulador+valor

promedio=acumulador/len(lista)
#imprimimos la lista
print(lista)
#imprimimos el promedio
print(promedio)
may = 0
for z in range(5):
    if lista[z]>promedio: may+=1
men=len(lista)-may
print(may," Son los mayores al promedio")
print(men," Son los menores al promedio")
