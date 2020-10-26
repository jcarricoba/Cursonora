'''
Autor: Jacobo Carricoba
Fecha de inicio: 13-10-2020
Objetivo: Crear una APP que almacene los cursos que esta realizando el usuario y ampliar y afianzar los conocimientos de Python del autor.
Nombre APP: Cursonora
'''
#-----------Importamos tkinter, tkinter para ventanas emergentes y la clase curfrom tkinter import *
from tkinter import *
from tkinter import messagebox
from clasecurso import curso
from sqlite3

#creamos raiz y un frame para el formulario de entrada
ventanafondo=Tk()
ventanafondo.title("Cursonora by J")
#formNuevocurso=Frame(ventanafondo)
#formNuevocurso.pack()
#formNuevocurso.config(width="300",height="100")

#Creamos un menú en la barra superior
'''
barraMenu = Menu(ventanafondo)
ventanafondo.config (menu = barraMenu, width="300",height="300")
archivoMenu=Menu(barraMenu,tearoff="0")
barraMenu.config(menu=barraMenu)
archivoMenu.add_command("Nuevo",command=nuevocurso)

def nuevocurso(self):
    pass

archivoEdicion=Menu(barraMenu, TearOff=0)
archivoSobre=Menu(barraMenu,TearOff=0)


barraMenu.add_cascade(Label="Archivo",menu=archivoEdicion)
barraMenu.add_cascade(Label="Info",menu=archivoSobre)

'''
#loop de raiz
ventanafondo.mainloop()
