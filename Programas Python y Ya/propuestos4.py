#TEMA 4: Estructura de datos tipo lista
#PROBLEMAS PROPUESTOS
#DIEGO LEON GOVEA ORTIZ

#Programa 1

lista = [100,200,300,50,40,200,20]

x=0
mayores=0
while x<len(lista):
    if lista[x]>100:
        print("El valor ",lista[x]," es mayor a 100")
        mayores+=1
    x=x+1

print("Numeros mayores a 100: ",mayores)

#Programa 2
