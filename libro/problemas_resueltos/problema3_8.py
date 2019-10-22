print("Serie ULAM")
NUM=int(input("Ingrese un numero"))
if NUM>0:
    while(NUM!=1):
        print(int(NUM))
        if (((-1)**NUM)>0):
            NUM=(NUM/2)
        else:
            NUM=((NUM*3)+1)
    print(int(NUM))
else:
    print("Escribe un entero positivo")
WAIT=input("Fin")
