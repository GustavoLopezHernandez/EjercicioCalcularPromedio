from abc import ABC, abstractmethod

class Alumno(ABC):

   def __init__(self, nombre, apellido, matricula, grado):
       self.nombre = nombre
       self.apellido = apellido
       self.matricula = matricula
       self.grado = grado

   def datosAlumno(self):
        pass

   @abstractmethod
   def calcularPromedio(self):
       pass

class Primaria(Alumno):

   def __init__(self, nombre, apellido, matricula, grado, cal1, cal2, cal3, cal4):
       Alumno.__init__(self, nombre, apellido, matricula, grado)
       self.nombre = nombre
       self.apellido = apellido
       self.matricula = matricula
       self.grado = grado

   def datosAlumno(self):
        print('Nombre: ', self.nombre)
        print('Apellido: ', self.apellido)
        print('Matricula: ', self.matricula)
        print('Grado: ', self.grado)

   def calcularPromedio(self):
      self.calt = (cal1 + cal2 + cal3 + cal4) / 4
      if self.calt >= 6:
          self.redondear = self.calt + .01
          self.redondear2 = round(self.redondear, 0)
          print('Su promedio es : ', self.calt)
          print('Su promedio se redondea a: ', self.redondear2)
          print('!Ha aprobado la materia, felicidades! :)')
      else:
          print('Su promedio es: 5')#En primaria si se reprueba no se pone el promedio, en automatico este es 5
          print('!Ha reprobado la materia :(')

class Secundaria(Alumno):

   def __init__(self, nombre, apellido, matricula, grado, cal1, cal2, cal3, cal4, cal5):
       Alumno.__init__(self, nombre, apellido, matricula, grado)
       self.nombre = nombre
       self.apellido = apellido
       self.matricula = matricula
       self.grado = grado

   def datosAlumno(self):
        print('Nombre: ', self.nombre)
        print('Apellido: ', self.apellido)
        print('Matricula: ', self.matricula)
        print('Grado: ', self.grado)

   def calcularPromedio(self):
      self.calt = (cal1 + cal2 + cal3 + cal4 + cal5) / 5
      if self.calt >= 7:
          self.redondear = self.calt - .01
          self.redondear2 = round(self.redondear, 0)
          print('Su promedio es: ', self.calt)
          print('Su promedio se redondea a: ', self.redondear2)
          print('!Ha aprobado la materia, felicidades! :)')
      else:
          print('Su promedio es: ', self.calt)
          print('!Ha reprobado la materia :(')

opc = int(input('Escriba 1 para Primaria - Escriba 2 para Secundaria '))

if opc == 1:
    nombre = str(input('Introduzca su nombre:  '))
    apellido = str(input('Introduzca su apellido: '))
    matricula = str(input('Introduzca su matricula: '))
    grado = int(input('Indroduzca su grado con numero: '))
    cal1 = float(input('Esciba la caficicacion del trimestre 1: '))
    cal2 = float(input('Esciba la caficicacion del trimestre 2: '))
    cal3 = float(input('Esciba la caficicacion del trimestre 3: '))
    cal4 = float(input('Esciba la caficicacion del trimestre 4: '))
    prim = Primaria(nombre, apellido, matricula, grado, cal1, cal2, cal3, cal4)
    prim.datosAlumno()
    prim.calcularPromedio()

if opc == 2:
    nombre = str(input('Introduzca su nombre:  '))
    apellido = str(input('Introduzca su apellido: '))
    matricula = str(input('Introduzca su matricula: '))
    grado = int(input('Indroduzca su grado con numero: '))
    cal1 = float(input('Esciba la caficicacion del bimestre 1: '))
    cal2 = float(input('Esciba la caficicacion del bimestre 2: '))
    cal3 = float(input('Esciba la caficicacion del bimestre 3: '))
    cal4 = float(input('Esciba la caficicacion del bimestre 4: '))
    cal5 = float(input('Esciba la caficicacion del bimestre 5: '))
    secu = Secundaria(nombre, apellido, matricula, grado, cal1, cal2, cal3, cal4, cal5)
    secu.datosAlumno()
    secu.calcularPromedio()
