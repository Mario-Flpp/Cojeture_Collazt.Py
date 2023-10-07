import tkinter as tk

def conjetura_collatz(numero):
    result_text.config(state=tk.NORMAL)  # Habilitar el widget de texto para edición
    result_text.delete(1.0, tk.END)  # Borrar contenido anterior
    
    while numero != 1:
        result_text.insert(tk.END, str(numero) + "\n")  # Agregar el número a la secuencia
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = (numero * 3) + 1
    
    result_text.insert(tk.END, "1\n")  # Agregar el último número (1)
    result_text.config(state=tk.DISABLED)  # Deshabilitar el widget de texto

def start_collatz():
    numero_inicial = int(entry.get())
    conjetura_collatz(numero_inicial)

# Crear la ventana
window = tk.Tk()
window.title("Conjetura de Collatz")
window.configure(bg="black")  # Fondo en modo oscuro

# Etiqueta y entrada para el número inicial
label = tk.Label(window, text="Número inicial:", bg="black", fg="white")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Botón para comenzar la conjetura
start_button = tk.Button(window, text="Calcular", command=start_collatz, bg="black", fg="white")
start_button.pack()

# Widget de texto para mostrar la secuencia
result_text = tk.Text(window, wrap=tk.WORD, width=80, height=30, bg="black", fg="white", state=tk.DISABLED)
result_text.pack()

# Iniciar la aplicación
window.mainloop()
