P = float(input("Ingrese una variable entera:"))
Q = float(input("Ingrese otra variable de tipo entero:"))
EXP= P**3+ Q**4-2*P**2
if EXP < 680:
    print(f"La primera variable es: {P} y la segunda variable es: {Q}")
else:
    print("Las variables no satisfacen la expresion")
print("fin del programa")
