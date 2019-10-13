print("ingrese 3 numeros: A, B y C")
A = float(input("Ingrese valor A:"))
B = float(input("Ingrese valor B:"))
C = float(input("Ingrese valor C:"))
if A<B:
    if B<C:
        print("Los numeros estan en orden creciente")
    else:
        print("los numeros no van en orden creciente")
else:
    print("los numeros no van en orden creciente")
print("Fin del programa")
