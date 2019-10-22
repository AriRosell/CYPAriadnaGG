print("Calcular el aumento de sueldo")
NOM=float(0)
SUE=float(input("Ingresa el sueldo"))
while (SUE!=(-1)):
    if SUE<1000:
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.12
    NOM=NOM+NSUE
    print("El nuevo sueldo es:",NSUE)
    SUE=float(input("Ingresa otro sueldo"))
print("La nomina es:",NOM)
WAIT=input("Fin del programa")
