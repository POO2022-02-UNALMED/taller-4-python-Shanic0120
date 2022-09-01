

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None,grado=None):
        self._grupo = grupo
        self.grado="Grado "+str(grado)
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = sorted([alumno]+lista)

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    """@ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre"""
