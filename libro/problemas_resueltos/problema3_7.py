print("Conocer las ventas")
CHI=int(0)
MED=int(0)
GRA=int(0)
N=int(input("Ingrese el numero de ventas: "))
I=int(1)
for I in range(0,N,1):
    V=float(input("Ingrese el valor de una venta: "))
    if V<=200:
        CHI=CHI+1
    else:
        if V<400:
            MED=MED+1
        else:
            GRA=GRA+1
    I=I+1
print("Las ventas menores o iguales a 200 son:",CHI)
print("Las ventas entre 200 y 400 son:",MED)
print("Las ventas mayores a 400 son:",GRA)
WAIT=input("Fin del programa")
