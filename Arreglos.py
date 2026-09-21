""" #Declarando un arreglo
numeros = [10, 20, 30, 40, 50]

#Imprimo un elemento espe. del arreglo
print(numeros[2])

#Reasignación
numeros[3]=35
print(numeros)

#Agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)

#Elimanos un valor en el arreglo
numeros.remove(35)
print(numeros)

#Eliminamos el valor de un arreglo usando la posición
numeros.pop(4)
print(numeros)

frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)

#Eliminamos un elemento del arreglo usando el nombre
frutas.remove("Manzana")
print(frutas)

#Declaración de un arreglo vacio
arreglo = []
print(arreglo)

n = int(input("Ingrese el tamaño el arreglo: "))
print(arreglo)

for i in range(n):
    dato = int(input("Ingrese un nmero: "))
    arreglo.append(dato)

print("El arreglo es:", arreglo)

n = int(input("Ingrese el tamaño del arreglo: "))

arreglo = [0] * n

for i in range(n):
        dato = int(input("Ingrese un número"))
        arreglo[i] = dato

print(arreglo)
"""
original = []
print("Introduce 15 números enteros (entre 0 y 500):")
for i in range(15):
    num = int(input(f"Número {i + 1}: "))
    original.append(num)

cincuerizado = [num if num % 5 == 0 else num + (5 - (num % 5)) for num in original]

print("\nArray original:    ", *original)
print("Array cincuerizado:", *cincuerizado)