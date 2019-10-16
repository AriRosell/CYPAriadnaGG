print("Encontrar el numero mayor")
A = float(input("Ingrese valor A: "))
B = float(input("Ingrese valor B: "))
C = float(input("Ingrese valor C: "))
if A>B:
    if A>C:
        print("A es el mayor")
    else:
        if A==C:
            print("A y C son los mayores")
        else:
            print("C es el mayor")
else:
    if A==B:
        if A>C:
            print("A y B son los mayores")
        else:
            if A==C:
                print("A, B y C son iguales")
            else:
                print("C es el mayor")
    else:
        if B>C:
            print("B es el mayor")
        else:
            if B==C:
                print("B y C son los mayores")
            else:
                print("C es el mayor")
print("Fin del Programa")
