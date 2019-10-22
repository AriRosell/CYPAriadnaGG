print("Numeros mayores que 0, promedio de positivos y promedio de todos")
SUMPOS=float(0)
CUEPOS=float(0)
SUMOTR=float(0)
N=int(input("Ingrese cuantos datos se van a leer: "))
I=int(1)
for I in range(0,N,1):
    NUM=float(input("Ingrese un Número: "))
    if NUM>0:
        SUMPOS=SUMPOS+NUM
        CUEPOS=CUEPOS+1
    else:
        SUMOTR=SUMOTR+NUM
    I=I+1
PROGEN=(SUMPOS+SUMOTR)/N
PROPOS=(SUMPOS/CUEPOS)
print("La cantidad de numeros positivos es:",CUEPOS)
print("El promedio de los positivos es:",PROPOS)
print("EL promedio de todo es:",PROGEN)
WAIT=input("Fin del programa")
