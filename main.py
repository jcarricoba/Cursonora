'''
Esta aplicación se crea para el autoapredizaje de Python de su autor, por lo que va comentada del siguiente modo:
Se añadirá un comentario con un número en el órden de creación, así posteriormente se podrá ver cómo el código crece de forma anidada.

Autor: Jacobo Carricoba González
Año: 2020
Licencia: No registrado
Uso: No comercial
Objetivo: Creación de una base de datos de cursos, con posibles estados de los mismos y 
la posibilidad de exportar un registro a un archivo de texto. Por ejemplo, para un CV.
Funciones: Añadir, modificar y borrar cursos (descripción, lugar donde se realiza, fecha inicio y fin, si está terminado o no 
y comentarios), guardará una bbdd de backup que se podrá recuperar en caso de borrado masivo o error de la principal.

'''
#0. Importamos el GUI Tkinter, con la función de messagebox que va aparte. También importamos las funciones de sqlite.
from tkinter import *
from tkinter import messagebox
#14. Importamos SQLite3 para gestionar la bbdd y os.path para comprobar si existe ya una bbdd creada
import sqlite3
import os.path


#1.creamos ventana y le ponemos título, posteriormente ponemos también el icono 
venroot=Tk()
venroot.title("Cursonora")
imgicon=PhotoImage(file="./images/birrete.ico")#PTE REVISAR ESTO, NO SE VE
venroot.iconphoto(False,imgicon)
#venroot.call("wm", "iconphoto", venroot._w, imgicon) 
#2.le asignamos una barra de menú a la ventana creada
barraMenu=Menu(venroot)

#3.configuramos ventana principal
venroot.config(menu=barraMenu,bg="blue")#6.b al crear el frame, ya no necesitamos indicar width="300", height="300"

#---------------------SUBMENUS (creación)
#5.creamos submenus, primero creamos variables que asignamos a la barra, abajo, con los add_command, les daremos nombre y les asignaremos una función
menuArchivo=Menu(barraMenu,tearoff=0)
menuOpciones=Menu(barraMenu,tearoff=0)
menuAyuda=Menu(barraMenu,tearoff=0)



#----------------------FUNCIONES
#13. He creado un archivo aparte para las funciones de esta aplicación (dentro de una carpeta "bin"). Le he llamado Funciones.py y la vamos a importar aquí bajo el nombre de Funciones.
#de este modo, para llamar a una función desde los command de los botones y menús, bastará con poner Funciones.Nombredelafunciónenelotroarchivo.
import bin.Funciones as Funciones


#5b Esta función es la comodín, sacará un popup || Eureka "hola mundo" || en lo que vamos definiendo cada función
#def Eureka():
#	messagebox.showinfo("Eureka", "Hola Mundo")
#NOTA: Al crear el archivo de funciones, la función comodín paso a ser "Funciones.UnaCualquiera"

#Llamamos a la función que crea la BBDD (si ya está creada no hace nada)
Funciones.CreandoBBDD()

#Incluimos una función para confirmar que se desea cerrar el programa
def deseasalir():
	OpcionElegida=Funciones.Salir()
	if OpcionElegida=="yes":
		venroot.destroy()
	else:
		return

#----------------------SUBMENUS (configuración)
#5c los add_command	
menuArchivo.add_command(label="¿Hay algo que meter aquí?",command=Funciones.UnaCualquiera)
menuArchivo.add_command(label="Guardar los cambios",command=Funciones.UnaCualquiera)
menuArchivo.add_separator()
menuArchivo.add_command(label="Eliminar Base de datos",command=Funciones.UnaCualquiera)
menuAyuda.add_command(label="Restaurar desde backup",command=Funciones.UnaCualquiera)
menuAyuda.add_command(label="Acerca de Cursonora",command=Funciones.UnaCualquiera)
menuOpciones.add_command(label="Listar cursos actuales",command=Funciones.UnaCualquiera)
menuOpciones.add_command(label="Exportar lista cursos",command=Funciones.UnaCualquiera)
menuOpciones.add_command(label="Duplicar curso actual",command=Funciones.UnaCualquiera)

#4.creamos menus y los relacionamos con sus submenus
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
barraMenu.add_cascade(label="Edición",menu=menuOpciones)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)

#6.creamos un frame para meter dentro el formulario de entrada
venframe=Frame(venroot)
venframe.pack()
venframe.config(width="300",height="300",bg="orange")
venframe.grid(column=0,row=0,sticky="nsew",padx="5",pady="15",columnspan="10") #mete el frame en la esquina superior izquierda, con el sticky permitimos la expansión, deja un pequeño margen a los bordes y ocupa 5 columnas del grid, de modo en que podremos situar las entradas de texto.
venroot.columnconfigure(0,weight="3") #hace que el frame se expanda en vertical si se cambia el tamaño de la ventana
venroot.rowconfigure(0,weight="1") #lo mismo en horizontal


#7 el GRID del programa consistirá en 4 columnas y 5 filas, comenzamos por la del medio, los cuadros de entrada (3 entry, 1 checkbox, 1 textbox)

entryIDcurso=Entry(venframe)
entryIDcurso.config(width="10",font="14",fg="BLUE",bg="GREY")
entryIDcurso.grid(row=0,column=1,padx=10,pady=5,sticky="W")

entryNombrecurso=Entry(venframe)
entryNombrecurso.config(font="14",fg="BLUE")
entryNombrecurso.grid(row=1,column=1,padx=10,pady=5)

entryLugar=Entry(venframe)
entryLugar.config(font="14",fg="BLUE")
entryLugar.grid(row=2,column=1,padx=10,pady=5)

entryFechaInicio=Entry(venframe)
entryFechaInicio.config(font="14",fg="BLUE")
entryFechaInicio.grid(row=3,column=1,padx=10,pady=5)

entryFechaFin=Entry(venframe)
entryFechaFin.config(font="14",fg="BLUE")
entryFechaFin.grid(row=4,column=1,padx=10,pady=5)

#creamos una variable que almacene el valor del checkbox
ccheckFinalizado=BooleanVar()
checkFinalizado=Checkbutton(venframe,variable=ccheckFinalizado)
checkFinalizado.grid(row=5,column=1,padx=10,pady=1,sticky=W+N)

TextComentario=Text(venframe,width=20,height=5)
TextComentario.grid(row=6,column=1,pady=5)

Scrollvertical=Scrollbar(venframe,command=TextComentario.yview)
Scrollvertical.grid(row=6,column=2,sticky="nsew")

TextComentario.config(font="14",fg="BLUE",yscrollcommand=Scrollvertical.set)

#8. Creamos los label de la columna 0

labelID=Label(venframe)
labelID.config(text="ID Curso: ",bg="orange",fg="blue")
labelID.grid(row=0,column=0,sticky="E")


labelNombre=Label(venframe)
labelNombre.config(text="Título: ",bg="orange",fg="blue")
labelNombre.grid(row=1,column=0,sticky="E")


labelLugar=Label(venframe)
labelLugar.config(text="Impartido por: ",bg="orange",fg="blue")
labelLugar.grid(row=2,column=0,sticky="E")


labelFechaI=Label(venframe)
labelFechaI.config(text="Fecha Inicio (Ej. 04/2020): ",bg="orange",fg="blue")
labelFechaI.grid(row=3,column=0,sticky="E")


labelFechaF=Label(venframe)
labelFechaF.config(text="Fecha Finalización (Ej. 05/2020): ",bg="orange",fg="blue")
labelFechaF.grid(row=4,column=0,sticky="E")


labelTerminado=Label(venframe)
labelTerminado.config(text="¿Finalizado?",bg="orange",fg="blue")
labelTerminado.grid(row=5,column=0,pady="10",sticky="E")


labelComentario=Label(venframe)
labelComentario.config(text="Comentarios: ",bg="orange",fg="blue")
labelComentario.grid(row=6,column=0,sticky="NE")

#9. Introducimos 1 botón para buscar debajo de los campos

botonBuscar=Button(venframe)
botonBuscar.config(text="Buscar",fg="blue",command=Funciones.UnaCualquiera)
botonBuscar.grid(row=7,column=1,padx=10,pady=5,sticky="W")


#10. Añado dos botones abajo, fuera del frame, el botón salir ya funciona.
botonBorrarCampos=Button(venroot)
botonBorrarCampos.config(text="Borrar Campos",fg="blue",command=Funciones.UnaCualquiera)
botonBorrarCampos.grid(row=8,column=0,padx="10",pady="10",sticky="W")

#añadimos lambda antes de la función para evitar que se ejecute antes de tiempo
botonGuardar=Button(venroot)
botonGuardar.config(text="Guardar",fg="blue",command=lambda:Funciones.Guardar(entryIDcurso.get(),entryNombrecurso.get(),entryLugar.get(),entryFechaInicio.get(),entryFechaFin.get(),ccheckFinalizado.get(),TextComentario.get("1.0",END)))
botonGuardar.grid(row=8,column=1,padx="10",pady="10",sticky="W")

botonSalir=Button(venroot)
botonSalir.config(text="Salir",fg="blue",command=deseasalir)
botonSalir.grid(row=8,column=2,padx="10",pady="10",sticky="W")

#loop de la ventana (1.)
venroot.mainloop()

'''
Pendiente:
-Ver si es necesaria una clase para las propiedades de cada curso, creo que sería apropiado, ver clasecurso.py
-Ver cómo situar las entradas de texto, los botones y las labels en la ventana.
-Estudiar posibilidad de varios usuarios, en una app en local no tiene sentido
'''