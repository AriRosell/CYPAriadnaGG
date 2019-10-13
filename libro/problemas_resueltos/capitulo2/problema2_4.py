print("Calificaciones del alumno")
MAT = int(input("Matricula del alumno:"))
CAL1= float(input("Primera calificacion del alumno:"))
CAL2= float(input("Segunda calificacion del alumno:"))
CAL3= float(input("Tercera calificacion del alumno:"))
CAL4= float(input("Cuarta calificacion del alumno:"))
CAL5= float(input("Quinta calificacion del alumno:"))
PRO=(CAL1+CAL2+CAL3+CAL4+CAL5)/(5)
if PRO>=6 :
    print(MAT , PRO, "Aprobado")
else:
    print(MAT , PRO, "No aprobado")
print("Fin del programa")
