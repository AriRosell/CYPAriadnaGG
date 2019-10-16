print("Calcular el costo total del paciente")
TIPO=int(input("Ingrese la el tipo de enfermedad: "))
EDAD=int(input("Ingrese la edad el paciente: "))
DIAS=int(input("Ingrese la cantidad de dias que estuvo hospitalizado: "))
COST={1:25,2:16,3:20,4:32}
COSTOT=DIAS*COST[TIPO]
if (EDAD>=14)&(EDAD<=22):
    COSTOT=COSTOT*1.10
    FLAG=1
else:
    FLAG=0
print("El costo total es:",COSTOT)
print("Flag:",FLAG)
print("Fin del programa")
