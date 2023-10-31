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

lista = [7,5,8,7,1]

x=0
while x<len(lista):
    if lista[x]>=7:
        print("El valor ",lista[x]," es mayor o igual a 7")
    x=x+1

#Programa 3

lista = ['valeria','diego','juan','max','andrea']

x=0
while x<len(lista):
    if len(lista[x])>=5:
        print("El nombre ",lista[x]," tiene 5 o mas digito")
    else:
        print("El nombre ",lista[x]," tiene menos de 5 digitos")
    x=x+1
