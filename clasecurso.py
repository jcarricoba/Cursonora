
class curso():
    def __init__(self):
        IDcurso=stringvar()
        nombre_curso=stringvar()
        fechaini=stringvar()
        fechafin=stringvar()
        cursoURL=stringvar()
        comentariocurso=stringvar()
        terminado=False
        iniciado=False
    def iniciar(self,IDcurso):
        self.iniciado=True
    def terminar(self,IDcurso):
        self.terminado=True
    def listar(self):
        pass
#ver si esto realmente entra en la clase, porque podría ser una función fuera de la misma
    def seleccionar(self,IDcurso):
        pass
#Aqui se seleccionara un curso en concreto, mostrando los detalles del mismo