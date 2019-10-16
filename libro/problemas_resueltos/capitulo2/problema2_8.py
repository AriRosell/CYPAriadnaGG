print("Calcular el monto a pagar")
COMPRA=float(input("Ingrese el monto total de la compra en pesos: "))
if COMPRA<500:
    PAGAR=COMPRA
else:
    if COMPRA<=1000:
        PAGAR=(COMPRA)-(COMPRA*0.05)
    else:
        if COMPRA<=7000:
            PAGAR=(COMPRA)-(COMPRA*0.11)
        else:
            if COMPRA<=15000:
                PAGAR=(COMPRA)-(COMPRA*0.18)
            else:
                PAGAR=(COMPRA)-(COMPRA*0.25)
print("El total a pagar es: ",PAGAR)
print("Fin del Programa")
            
