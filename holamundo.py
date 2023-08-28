import tkinter as tk

# Crear Ventana Principal
root = tk.Tk()
root.title("HolaMundo")

# Crear etiqueta
label = tk.Label(root, text="Hola Mundo")
label.pack(pady=10)

# Start the main event loop
root.mainloop()
