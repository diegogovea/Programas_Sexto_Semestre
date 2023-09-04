import tkinter as tk

def mostrar_datos():
    for i, campo in enumerate(campos):
        valor = campo.get()
        print(f"Campo {i + 1}: {valor}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario con Botones")

# Crear los campos de entrada y botones
campos = []
botones = []

for i in range(4):
    etiqueta = tk.Label(ventana, text=f"Campo {i + 1}:")
    etiqueta.grid(row=i, column=0, padx=10, pady=5)
    campo = tk.Entry(ventana)
    campo.grid(row=i, column=1, padx=10, pady=5)
    boton = tk.Button(ventana, text="Mostrar", command=mostrar_datos)
    boton.grid(row=i, column=2, padx=10, pady=5)
    campos.append(campo)
    botones.append(boton)

# Iniciar la aplicación
ventana.mainloop()
