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



# Label para mostrar la ruta del archivo seleccionado
ruta_label = tk.Label(ventana, text="Ruta de archivo: ")
ruta_label.pack()

#Boton "Siguiente"
boton_siguiente = tk.Button(ventana, text="Siguiente", command=funcion_siguiente)
boton_siguiente.pack()

# Ejecutar la interfaz
ventana.mainloop()
