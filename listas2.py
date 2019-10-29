# arreglo
# lectura
# escritura / asignacion
# actualizacion : insercion, eliminacion , modificacion
# ordenamiento
# busqueda

# escritura
frutas = ["zapote", "manzana", "pera","aguacate","durazno","uva","sandia"]

# lectura, el selector [indice]
print(frutas[2])
# lectura con for
# for opcion 1
for indice in range(0,7,1):
    print(frutas[indice])
print("-----")

# for opcion 2 -- por un iterador for each

for fr in frutas:
    print(fr)

# asignacio
frutas[2]="melon"
print(frutas)

# insercion al final
frutas.append("naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"limon")
print(frutas)
print(len(frutas))
frutas.insert(0,"mamey")
print(frutas)

#eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

# busqueda
print(f"la uva esta en la pos. { frutas.index('uva') }")
print(f"el limon esta { frutas.count('limon') } veces en la lista")

#concatenar
print(frutas)
otras_frutas =["rambutan","nispero","liche","pitaya"]
frutas.extend(otras_frutas)
print(frutas)

# copiar

copia=frutas
copia.append("naranja")
print(frutas)
print(copia)

