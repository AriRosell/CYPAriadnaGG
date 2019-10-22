print("Calcula la serie")
N=int(input("Ingresa N: "))
I=int(1)
SERIE=float(0)
for I in range(I,N,1):
    SERIE=SERIE+(I**I)
    print(int(SERIE))
    I=I+1
print("El total de la serie es:",int(SERIE))
WAIT=input("FIN")
