print("Imprimir una serie")
SUMSER=int(0)
BAND='T'
I=2
while (I<=1800):
    SUMSER=SUMSER+I
    print(I)
    if (BAND=='T'):
        BAND='F'
        I=I+3
    else:
        BAND='T'
        I=I+2
print("La suma de la serie es:",SUMSER)
WAIT=input("Fin del programa")
