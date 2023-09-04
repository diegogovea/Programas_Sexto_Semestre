import tkinter as tk
import re


# Función para validar un RFC
def validar_rfc(campo, resultado_label):
    valor = campo.get()
    # Patrón de validación de RFC (México)
    rfc_pattern = r'^[A-Z]{3,4}[0-9]{6}[A-Z0-9]{3}$'
    if re.match(rfc_pattern, valor):
        resultado_label.config(text="Es un RFC válido")
    else:
        resultado_label.config(text="No es un RFC válido")

def validar_direccion_mac(campo, resultado_label):
    valor = campo.get().upper()  # Convertir a mayúsculas para comparar con el patrón
    # Patrón de validación de dirección MAC
    mac_pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    if re.match(mac_pattern, valor):
        resultado_label.config(text="Es una dirección MAC válida")
    else:
        resultado_label.config(text="No es una dirección MAC válida")

# Función para validar una dirección IP
def validar_direccion_ip(campo, resultado_label):
    valor = campo.get()
    # Patrón de validación de dirección IP (IPv4)
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(ip_pattern, valor):
        resultado_label.config(text="Es una dirección IP válida")
    else:
        resultado_label.config(text="No es una dirección IP válida")

# Función para validar si un campo contiene un número
def validar_numero(campo, resultado_label):
    valor = campo.get()
    if not valor.isdigit():
        resultado_label.config(text="No es un número")
    else:
        resultado_label.config(text="Es un número")


# Función para validar una URL
def validar_url(campo, resultado_label):
    valor = campo.get()

    # Patrón de validación de URL
    url_pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'

    if re.match(url_pattern, valor):
        resultado_label.config(text="Es una URL válida")
    else:
        resultado_label.config(text="No es una URL válida")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario con Botones para Validar RFC")

# Crear los campos de entrada y etiquetas de resultado
campos = []
resultado_labels = []

validacion_funciones = {
    0: validar_direccion_ip,
    1: validar_rfc,
    2: validar_direccion_mac,
    3: validar_url,
}

for i in range(4):
    etiqueta = tk.Label(ventana, text=f"Campo {i + 1}:")
    etiqueta.grid(row=i, column=0, padx=10, pady=5)
    campo = tk.Entry(ventana)
    campo.grid(row=i, column=1, padx=10, pady=5)
    resultado_label = tk.Label(ventana, text="")
    resultado_label.grid(row=i, column=2, padx=10, pady=5)
    campos.append(campo)
    resultado_labels.append(resultado_label)

    # Botón para validar el campo actual
    boton_validar = tk.Button(ventana, text=f"Validar",
                              command=lambda c=campo, r=resultado_label, f=validacion_funciones[i]: f(c, r))
    boton_validar.grid(row=i, column=3, padx=10, pady=5)

# Iniciar la aplicación
ventana.mainloop()
