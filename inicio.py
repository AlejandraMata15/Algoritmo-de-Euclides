import tkinter as tk
import os
from tkinter import Entry, StringVar
from tkinter import filedialog
from cryptography.fernet import Fernet

#Funcion para manejar la seleccion de radio buttons
def seleccion_radio():
    global opcion_seleccionada
    opcion_seleccionada = var.get()

#Funcion que se ejecutara al presionar el boton "Siguiente"
def funcion_siguiente():
    if opcion_seleccionada == "Cifrar":
        cifrar(archivo_seleccionado)

    elif opcion_seleccionada == "Descifrar":
        descifrar(archivo_seleccionado)


    
# Crear la ventana
ventana = tk.Tk()
ventana.title("Práctica 1")
ventana.geometry("500x300")
#ventana.configure(bg="gray")  # Establecer el color de fondo en gris

#Variables
opcion_seleccionada = None
salto = StringVar()
archivo_seleccionado = None
nuevo_archivo = None

#Label para n
label_n = tk.Label(ventana, text="n: ")
label_n.pack()

#Entry para ingresar el valor de salto
entry_n = Entry(ventana, textvariable=n)
entry_n.pack()

#Label para alpha
label_alpha = tk.Label(ventana, text="Alpha: ")
label_alpha.pack()

#Entry para ingresar el valor de salto
entry_alpha = Entry(ventana, textvariable=alpha)
entry_alpha.pack()

#Label para beta
label_beta = tk.Label(ventana, text="beta: ")
label_salto.pack()

#Entry para ingresar el valor de salto
entry_beta = Entry(ventana, textvariable=beta)
entry_beta.pack()


# Label para mostrar la ruta del archivo seleccionado
ruta_label = tk.Label(ventana, text="Ruta de archivo: ")
ruta_label.pack()

#Boton "Siguiente"
boton_siguiente = tk.Button(ventana, text="Siguiente", command=funcion_siguiente)
boton_siguiente.pack()

# Ejecutar la interfaz
ventana.mainloop()
