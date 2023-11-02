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

#Programa 2: Vocales

oracion = input("Ingresa una cadena ---> ")

print(oracion)
a=0
e=0
o=oracion.lower()

for a in range(len(o)):
    if o[a]   == "a":e+=1
    elif o[a] == "e":e+=1
    elif o[a] == "i":e+= 1
    elif o[a] == "o":e+= 1
    elif o[a] == "u":e+= 1

    a+=1

print("Hay ",e," vocales")
