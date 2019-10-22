print("calcular la serie")
SERIE=0
N=int(input("Escribe N: "))
BAND='T'
I=int(1)
for I in range(1,N,1):
    if (BAND=='T'):
        SERIE=SERIE+(1/I)
        BAND='F'
    else:
        SERIE=SERIE-(1/I)
        BAND='T'
    I=I+1
print("La suma de la serie es:",SERIE)
WAIT=input("Fin del programa")
    
        
