import tkinter as tk
import os
from tkinter import Entry, StringVar
from tkinter import filedialog
from cryptography.fernet import Fernet

#Funcion que se ejecutara al presionar el boton "Siguiente"
def funcion_aee():
    n=n.get()
    alpha=alpha.get()
    beta=beta.get()
    print(n)
    print(alpha)
    print(beta)
    
# Crear la ventana
ventana = tk.Tk()
ventana.title("Práctica 1")
ventana.geometry("500x300")
#ventana.configure(bg="gray")  # Establecer el color de fondo en gris

#Variables
n = StringVar()
alpha = StringVar()
beta = StringVar()

#Label para n
label_n = tk.Label(ventana, text="n: ")
label_n.pack()

#Entry para ingresar el valor de n
entry_n = Entry(ventana, textvariable=n)
entry_n.pack()

#Label para alpha
label_alpha = tk.Label(ventana, text="Alpha: ")
label_alpha.pack()

#Entry para ingresar el valor de alpha
entry_alpha = Entry(ventana, textvariable=alpha)
entry_alpha.pack()

#Label para beta
label_beta = tk.Label(ventana, text="beta: ")
label_beta.pack()

#Entry para ingresar el valor de beta
entry_beta = Entry(ventana, textvariable=beta)
entry_beta.pack()


# Label para mostrar la ruta del archivo seleccionado
ruta_label = tk.Label(ventana, text="Ruta de archivo: ")
ruta_label.pack()

#Boton "Siguiente"
boton_generarFunciones = tk.Button(ventana, text="Generar Funciones", command=funcion_aee)
boton_generarFunciones.pack()

# Ejecutar la interfaz
ventana.mainloop()
