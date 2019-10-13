print("Ingrese los valores de A, B y C en una ecuacion de segundo grado")
A = float(input("Ingrese valor A:"))
B = float(input("Ingrese valor B:"))
C = float(input("Ingrese valor C:"))
DIS= B**2-4*A*C
if DIS>=0:
    X1=((-B)+(DIS**0.5))/(2*A)
    X2=((-B)-(DIS**0.5))/(2*A)
    
    print(f"La primera raiz de la ecuacion es: {X1}, y la segunda raiz de la ecuacion es: {X2}")
else:
    print("Los valores son imaginarios")
print(f"Calculo auxiliar: {DIS}")
print("Fin del programa")
