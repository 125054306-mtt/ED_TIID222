matriz = [
    [73, 12, 9, 34],
    [5, 61, 27, 94],
    [46, 18, 0, 3]
]
matriz.append([26,93,14,33])
print(matriz)
print(matriz[1])

for i in matriz:
    if 61 in i:
        print(f"61 encontrado en la fila {i}")
        break


for filas in matriz:
    for numeros in filas:
        if numeros == 18:
            print(f"18 econtrado en {filas}")
            break
