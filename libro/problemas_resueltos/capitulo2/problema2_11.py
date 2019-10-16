print("Calcular el costo total de la llamada")
CLAVE=float(input("Ingrese la Clave: "))
NUMIN=float(input("Ingrese la duracion de la llamada en minutos: "))
CLAVES = {12: 2, 15: 2.2, 18: 4.5, 19: 3.5, 23: 6, 25: 6, 29: 5}
PRECIO=CLAVES [CLAVE]
COST= NUMIN*PRECIO
print("El Costo total de la llamada es: ",COST)
print("Fin del programa")

