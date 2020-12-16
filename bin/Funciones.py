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

def Buscar(IDc,Nomc,Lugc):
	Datos=[IDc,Nomc,Lugc]
	#messagebox.showinfo("control",IDc+" "+Nomc+" "+Lugc)
	if (IDc==""):
		if (Nomc!=""):
			if (Lugc!=""):
				try:
					Datos=Nomc,Lugc
					laConexion=sqlite3.connect("Gestordecursos")
					elPuntero=laConexion.cursor()
					elPuntero.execute("SELECT IDCurso,NOMBRE_CURSO FROM DATOSCURSOS WHERE NOMBRE_CURSO LIKE ? AND LUGAR_CURSO LIKE ?",('%'+str(Datos[0])+'%','%'+str(Datos[1])+'%',))
					resultados=elPuntero.fetchall()
					if (len(resultados))<2:
						elPuntero.execute("SELECT IDCurso,NOMBRE_CURSO FROM DATOSCURSOS WHERE NOMBRE_CURSO LIKE ? AND LUGAR_CURSO LIKE ?",('%'+str(Datos[0])+'%','%'+str(Datos[1])+'%'))
						resultados2=elPuntero.fetchall
						return(resultados2)
					else:
						messagebox.showinfo("INFO","Introduce el número identificador del curso en el campo IDCurso entre los siguientes: \n " + str(resultados))
						return("no")
				except:
					messagebox.showwarning("ATENCIÓN!","Algo ha ido mal en la consulta")
					return "no"
			else:
				try:
					Datos=Nomc
					laConexion=sqlite3.connect("Gestordecursos")
					elPuntero=laConexion.cursor()
					elPuntero.execute("SELECT IDCurso,NOMBRE_CURSO FROM DATOSCURSOS WHERE NOMBRE_CURSO LIKE ?",('%'+str(Datos[0])+'%',))
					resultados=elPuntero.fetchall()
					if (len(resultados)<2):
						elPuntero.execute("SELECT * FROM DATOSCURSOS WHERE LUGAR_CURSO LIKE ?",('%'+str(Datos[0])+'%',))
						resultados2=elPuntero.fetchall()
						return(resultados2)
					elif (len(resultados)>1):
						messagebox.showinfo("INFO","Introduce el número identificador del curso en el campo IDCurso entre los siguientes: \n" + str(resultados))
						return "no"
					else:
						messagebox.showwarning("ATENCIÓN!","No se encontró ningún registro con ese dato")	
						return "no"
				except:
					messagebox.showwarning("ATENCIÓN!","Algo ha ido mal en la consulta")
					return "no"
		elif (Lugc!=""):
			try:
				Datos=Lugc
				laConexion=sqlite3.connect("Gestordecursos")
				elPuntero=laConexion.cursor()
				elPuntero.execute("SELECT IDCurso,NOMBRE_CURSO FROM DATOSCURSOS WHERE LUGAR_CURSO LIKE ?",('%'+str(Datos)+'%',))
				resultados=elPuntero.fetchall()
				if (len(resultados)<2):
					elPuntero.execute("SELECT * FROM DATOSCURSOS WHERE LUGAR_CURSO LIKE ?",('%'+str(Datos)+'%',))
					resultados2=elPuntero.fetchall()
					return(resultados2)
				elif (len(resultados)>1):
					messagebox.showinfo("INFO","Introduce el número identificador del curso en el campo IDCurso entre los siguientes: \n" + str(resultados))
					return "no"
				else:
					messagebox.showwarning("ATENCIÓN!","No se encontró ningún registro con ese dato")
					return("no")
			except:
				messagebox.showwarning("ATENCIÓN!","Algo ha ido mal con la consulta")
				return "no"	
	else:
		try:
			Datos=IDc
			laConexion=sqlite3.connect("Gestordecursos")
			elPuntero=laConexion.cursor()
			elPuntero.execute("SELECT * FROM DATOSCURSOS WHERE IDCurso=?", (Datos[0],))
			resultados=elPuntero.fetchall()
			if (len(resultados)<2 and len(resultados)>0):
				return(resultados)
			else:
				messagebox.showwarning("ATENCIÓN!","No se encontró ningún registro con ese dato")
				return("no")
		except:
			messagebox.showwarning("ATENCIÓN!","Algo ha ido mal con la consulta")
			return "no"