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

#Funcion de cifrado
def cifrar(archivo):
    print("Cifrando...")
    archivo = renombrar_archivo(archivo)
    #Genera un codigo bien grande(llave)
    clave=Fernet.generate_key()
    archClave= open('llave.key', 'rb')
    archClave.write(clave)
    f=Fernet(clave)
    arch=open(archivo,'rb')
    encript=f.encrypt(arch.read())
    archivo = agregar_extension_c(archivo)
    print(archivo)
    salida= open(archivo,'wb')
    print(archivo)
    salida.write(encript)

def agregar_extension_c(archivo):
    archivo = archivo[:archivo.index('.')]+'_c.txt'
    return archivo

def agregar_extension_d(archivo):
    archivo = archivo[:archivo.index('.')]+'_d.txt'
    return archivo

def descifrar(archivo):
    print("Descifrando")
    archivo = renombrar_archivo(archivo)
    archClave=open('llave.key', 'rb')
    f=Fernet(archClave.read())
    arch=open(archivo,'rb')
    dec=f.decrypt(arch.read())
    archivo = agregar_extension_d(archivo)
    print(archivo)
    salida=open(archivo,'wb')
    salida.write(dec)

def nombre(archivo):
    cadena_original = os.path.basename(archivo)
    return cadena_original

# Función para manejar la selección de archivo
def seleccionar_archivo():
    global archivo_seleccionado
    archivo_seleccionado = filedialog.askopenfilename()
    ruta_label.config(text="Ruta de archivo: " + archivo_seleccionado)
   
def renombrar_archivo(archivo):
        ruta = archivo[::-1]
        ruta[:ruta.index('/')]
        ruta = ruta[:ruta.index('/')]
        print(ruta[::-1])
        ruta= ruta[::-1]
        return ruta
    
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

#Radio Buttons
var = tk.StringVar()
var.set(None) #Iniciar sin valor seleccionado
radio_cifrar = tk.Radiobutton(ventana, text="Cifrar", variable=var,value="Cifrar", command=seleccion_radio)
radio_descifrar = tk.Radiobutton(ventana, text="Descifrar", variable=var, value="Descifrar", command=seleccion_radio)

radio_cifrar.pack()
radio_descifrar.pack()


# Botón "Seleccionar archivo"
boton_seleccionar = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton_seleccionar.pack()

# Label para mostrar la ruta del archivo seleccionado
ruta_label = tk.Label(ventana, text="Ruta de archivo: ")
ruta_label.pack()

#Boton "Siguiente"
boton_siguiente = tk.Button(ventana, text="Siguiente", command=funcion_siguiente)
boton_siguiente.pack()

# Ejecutar la interfaz
ventana.mainloop()
