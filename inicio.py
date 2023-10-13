import mcd as f
import tkinter as tk
import os
from tkinter import Entry, StringVar
from tkinter import filedialog

def borrarAvisador():
    salida.config(text='')

#Funciones de backend
def p2():
	ns=int(n.get())
	alphas=int(alpha.get())
	betas=int(beta.get())

	sal=f.inicio(ns,alphas,betas)
	salida.config(text=sal)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Práctica 2")
ventana.geometry("500x400")

#Label para n
label_n = tk.Label(ventana, text="n: ")
label_n.pack()

#Entry para ingresar el valor de n
n=tk.Entry(ventana,width=15)
n.pack()

#Label para alpha
label_alpha = tk.Label(ventana, text="Alpha: ")
label_alpha.pack()

#Entry para ingresar el valor de alpha
alpha=tk.Entry(ventana,width=15)
alpha.pack()

#Label para beta
label_beta = tk.Label(ventana, text="Beta: ")
label_beta.pack()

#Entry para ingresar el valor de beta
beta=tk.Entry(ventana,width=15)
beta.pack()

#Boton "Siguiente"
boton_generarFunciones = tk.Button(ventana, text="Generar Funciones",command=p2)
boton_generarFunciones.pack()

#Para mostrar la salida
salida=tk.Label(ventana,text='')
salida.pack()

# Ejecutar la interfaz
ventana.mainloop()
