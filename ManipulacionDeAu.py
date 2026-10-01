numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])

print("El número 95 ocupa la posición:", numeros.index(95))
print("El número 67 ocupa la posición:", numeros.index(67))