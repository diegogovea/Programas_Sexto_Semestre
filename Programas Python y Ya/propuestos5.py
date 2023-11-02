#TEMA 5: Procesar cadenas de caracteres
#PROBLEMAS PROPUESTOS
#DIEGO LEON GOVEA ORTIZ

#Programa 1: Recorrer oracion

oracion = input("Ingresa una cadena")

print(oracion)
a=0
e=0
for a in range(len(oracion)):
    if oracion[a]==" ":e+=1
    a+=1

print("Hay ",e," espacios")
