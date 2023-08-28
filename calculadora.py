# Función para sumar dos números
def suma(a, b):
    return a + b

# Función para restar dos números
def resta(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicacion(a, b):
    return a * b

# Función para dividir dos números
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

# Main
while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '5':
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida")
