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

#Programa 3: Contraseña
x=0
while x!=1:
    contra = input("Ingresa una contraseña ---> ")
    if len(contra) >= 10 and len(contra) <= 20:
        print("Tu contraseña es: ", contra)
        x=1
    else:
        print("Contraseña invalida, debe tener al menos 10 caracteres y menos de 20")
        x=0

