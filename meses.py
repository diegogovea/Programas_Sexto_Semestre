import tkinter as tk
from tkinter import messagebox

def get_month_name():
    try:
        month_number = int(entry.get())
        if 1 <= month_number <= 12:
            # Obtener el nombre del mes de la lista month_names
            month_name = month_names[month_number - 1]
            result_label.config(text=f"{month_name}")
        else:
            messagebox.showerror(
                "Error", "Por favor, ingresa un número en el rango válido (1-12).")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido.")

# Lista de nombres de los meses
month_names = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Crear la ventana principal
root = tk.Tk()
root.title("Práctica 3")

# Crear una etiqueta
label = tk.Label(root, text="Ingresa el número del mes (1-12):")
label.pack(pady=10)

# Crear una entrada
entry = tk.Entry(root)
entry.pack(pady=5)

# Crear un botón
button = tk.Button(root, text="Mostrar mes", command=get_month_name)
button.pack()

# Crear una etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Iniciar el bucle principal de eventos
root.mainloop()
