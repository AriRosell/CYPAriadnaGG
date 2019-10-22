print("Suma de los numeros impares y promedio de los pares")
SUMPAR=0
SUMIMP=0
CUEPAR=0
I=1
for I in range(0,270,1):
    NUM=int(input("Ingresa un numero"))
    if (NUM!=0):
        if (((-1)**NUM)>(0)):
            SUMPAR=SUMPAR+NUM
            CUEPAR=CUEPAR+1
        else:
            SUMIMP=SUMIMP+NUM
    I=I+1
PROPAR=SUMPAR/CUEPAR
print("La suma de los impares es:",SUMIMP)
print("El promedio de los pares es:",PROPAR)
WAIT=input("Fin del programa")
