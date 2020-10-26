from tkinter import messagebox
import sqlite3

#En este archivo irán todas las funciones de la aplicación, salvo aquellas pertenecientes a la clase, de haberlas.
def UnaCualquiera():
	messagebox.showinfo("Eureka","Esto era una prueba y fue bien!!")
#creamos una conexión a la bbdd y un puntero para trabajar sobre ella
def CreandoBBDD():
	laConexion=sqlite3.connect("Gestordecursos")
	elPuntero=laConexion.cursor()
#con el siguiente "try" en caso de error porque la bbdd ya exista.	
	try:
		elPuntero.execute('''
			CREATE TABLE DATOSCURSOS (
			IDCurso INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_CURSO VARCHAR(100),
			LUGAR_CURSO VARCHAR(100),
			FECHA_INI DATE,
			FECHA_FIN DATE,
			TERMINADO INTEGER(1),
			COMENTARIO TEXT(1000)
			)
		''')
		laConexion.commit()
		laConexion.close()
		messagebox.showinfo("INFO","Se ha generado una BBDD nueva")
	except:
		pass
	

def Guardar(IDc,Nomc,Lugc,FIc,FFc,Tc,Cc):
	Datos=Nomc,Lugc,FIc,FFc,Tc,Cc
	if (IDc!=""):
		messagebox.showwarning("Error","El campo IDCurso no está vacío")
	else:
		if (Nomc==""):
			messagebox.showwarning("Error","El campo Título es el único que no puede estar vacío")
		else:
			try:
				laConexion=sqlite3.connect("Gestordecursos")
				elPuntero=laConexion.cursor()
				elPuntero.execute("INSERT INTO DATOSCURSOS VALUES (NULL,?,?,?,?,?,?)",(Datos))
				laConexion.commit()
				messagebox.showinfo("INFO","Registro guardado")
			except:
				messagebox.showwarning("ATENCIÓN!","No se pudo registrar, revise los datos proporcionados")
	return

def Salir():
	Respuesta=messagebox.askquestion("Salir","¿Está seguro de querer salir?")
	return(Respuesta)