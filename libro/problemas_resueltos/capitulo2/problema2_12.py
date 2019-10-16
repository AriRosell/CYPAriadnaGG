print("Cuanto hay que pagar al trabajador")
SUE= float(input("Ingrese el sueldo del trabajador: "))
CATE= float(input("Ingrese la categoria del trabajador (Entre 1 y 8): "))
HE= float(input("Ingrese la cantidad de horas extras: "))
PHE = {1:30 , 2: 38, 3: 50, 4: 70, 5: 0, 6: 0, 7: 0, 8:0}
if HE>30:
    NSUE=SUE+30*(PHE[CATE])
else:
    NSUE=SUE+(HE*PHE[CATE])
print("La hora extra se paga en: ",PHE[CATE])
print("El Pago al trabajador es: ",NSUE)
print("Fin del Programa")
