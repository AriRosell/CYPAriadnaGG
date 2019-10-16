print("Calculo del precio mas impuestos")
PREBAS=float(input("Ingrese el precio del producto sin impuestos: "))
if PREBAS>500:
    IMP=(20*0.30)+((PREBAS-40)*(0.50))
else:
    if PREBAS>40:
        IMP=(20*0.30)+(PREBAS-40)*(0.40)
    else:
        if PREBAS>20:
            IMP=(PREBAS-20)*0.30
        else:
            IMP=0
PRETOT=PREBAS+IMP
print("El precio sin impuestos es: ",PREBAS)
print("Los impuestos son: ",IMP)
print("El precio con impuestos es: ",PRETOT)
print("Fin del programa")
