print("Determinar si es apto para una carrera")
MAT=int(input("Ingrese la Matricula del alumno: "))
CARR=str(input("Ingrese la carrera a la que aspira el alumno (en minusculas sin acentos): "))
SEM=int(input("Ingrese el semestre del alumno: "))
PROM=float(input("Ingrese el promedio del alumno: "))
PROMCARR={'economia':8.8,'computacion':8.5,'administracion':8.5,'contabilidad':8.5}
SEMCARR={'economia':6,'computacion':6,'administracion':5,'contabilidad':5}
if (SEM>SEMCARR[CARR])&(PROM>=PROMCARR[CARR]):
    print("El alumno:",MAT,"es apto para la carrera: ",CARR)
else:
    print("El alumno: ",MAT,"es no apto para la carrera:",CARR)
print("Fin del Programa")
