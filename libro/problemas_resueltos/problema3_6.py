print("Calcular el numero mayor y el menor")
MAY=int(-100000)
MEN=int(100000)
N=int(input("Ingrese la cantidad de numeros a ingresar: "))
I=int(1)
for I in range(0,N,1):
    NUM=int(input("Ingrese un numero: "))
    if NUM>MAY:
        MAY=NUM
    if NUM<MEN:
        MEN=NUM
    I=I+1
print("El numero mayor es:",MAY)
print("El numero menor es:",MEN)
WAIT=input("Fin del programa")
