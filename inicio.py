import tkinter as tk
import os
from tkinter import Entry, StringVar
from tkinter import filedialog
from cryptography.fernet import Fernet
import funciones as f

#Funcion que se ejecutara al presionar el boton "Siguiente"
def funcion_siguiente(): 
    valor_n=n.get()
    valor_alpha=alpha.get()
    valor_beta=beta.get()
    print(valor_n)
    print(valor_alpha)
    print(valor_beta)
    cifrado,descifrado=f.inicio(int(valor_n), int(valor_alpha), int(valor_beta))
    cifrado_label.config(cifrado)
    descifrado_label.config(descifrado)
    
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

# Label para mostrar la funcion de cifrado
cifrado_label = tk.Label(ventana, text="Funcion de cifrado: ")
cifrado_label.pack()

# Label para mostrar la funcion de descifrado
descifrado_label = tk.Label(ventana, text="Funcion de descifrado: ")
descifrado_label.pack()

#Boton "Siguiente"
boton_generarFunciones = tk.Button(ventana, text="Generar Funciones", command=funcion_siguiente)
boton_generarFunciones.pack()

# Ejecutar la interfaz
ventana.mainloop()
