import tkinter as tk
import random
from timeit import default_timer as timer


# Creamos la interfaz
raiz = tk.Tk()
raiz.title("Demuestra lo rapido que escribes")
raiz.geometry("800x500")
raiz.config(bg="#c9fff6")

# Establecemos las frases
frases = [
    "El rápido zorro marrón salta sobre el perro perezoso.",
    "Aprender a programar es un desafío divertido.",
    "Python es un lenguaje de programación versátil.",
    "Las interfaces gráficas hacen los programas interactivos."
]

inicio = None  # Variable global para el temporizador
frase = ""  # Variable global para la frase generada

# Funcion para generar y mostrar una frase al azar
def mostrar_frase():
    global frase
    frase = random.choice(frases)
    label2.config(text=frase, pady=5)
    
# Con esta funcion le damos la opcion al usuario de seleccionar todo el texto con control-a
def seleccionar_todo(event):
    """Seleccionar todo el texto en el campo de entrada."""
    entrada.select_range(0, tk.END) 
    return "break" 

# Funcion para validar la entrada del usuario y ver el tiempo de escritura
def validar_entrada(event):
    global inicio
    entrada_usuario = entrada.get()
    final = timer()
    tiempo_transcurrido = final - inicio if inicio else 0
    if entrada_usuario == frase:
        resultado = "Correcto"
    else:
        resultado = "Hay errores en tu escritura"
        
    label3.config(text=f"{resultado}\nTiempo: {tiempo_transcurrido:.2f} segundos")
    entrada.delete(0, "end")  # Limpiamos el campo de entrada independientemente de que el usuario escribe bien o mal el texto
    inicio = None  # Reiniciamos el temporizador para la próxima escritura del usuario

# Con esta funcion hacemos que el tiempo comience a contar desde que el usuario presione alguna tecla
def iniciar_temporizador(event):
    global inicio
    if inicio is None:  # Solo inicia el temporizador la primera vez
        inicio = timer()


label = tk.Label(raiz, text="Presiona el botón para iniciar la prueba",
                 font=("Times New Roman", 26, "bold underline"), pady=10, bg="#c9fff6")
label.place(relx=0.5, rely=0.04, anchor="center", relheight=0.058, relwidth=0.8)

boton = tk.Button(raiz, text="Presiona", font=20, command=mostrar_frase,
                  padx=30, pady=15, fg="red", bg="#b8ffa9")
boton.place(relx=0.5, rely=0.15, anchor="center", relheight=0.058, relwidth=0.15)

label2 = tk.Label(raiz, text="", font=("Helvetica", 16, "normal"),
                  bg="#c9fff6", height=2, width=60)
label2.place(relx=0.5, rely=0.25, anchor="center", relheight=0.058, relwidth=0.7)

label3 = tk.Label(raiz, text="", font=("Helvetica", 16, "normal"),
                  bg="#c9fff6", height=2, width=60, fg="red")
label3.place(relx=0.5, rely=0.47, anchor="center", relheight=0.1, relwidth=0.7)

entrada = tk.Entry(raiz, font=("TkDefaultFont", 12, "normal"))
entrada.place(relx=0.5, rely=0.35, anchor="center", relheight=0.06, relwidth=0.6)

# Asociar eventos
entrada.bind("<Control-a>", seleccionar_todo) # Selecciona todo el texto con control-a
entrada.bind("<Return>", validar_entrada) # El tiempo se para cuando el usuario presiona return(enter)
entrada.bind("<Key>", iniciar_temporizador)  # Detecta la primera tecla presionada

raiz.mainloop()
