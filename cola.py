# Ejercicio 1. Colas
repetir = "s"
 
while repetir == "s":
    cola = []
    opcion = 0
 
    while opcion != 4:
        print("\n--- MENÚ COLA ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")
 
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Escribe solo un número del 1 al 4.")
            opcion = 0
            continue
 
        if opcion == 1:
            try:
                numero = int(input("Escribe el número que quieres insertar: "))
                cola.append(numero)
                print("Número insertado en la cola.")
            except ValueError:
                print("Eso no es un número.")
        elif opcion == 2:
            if len(cola) == 0:
                print("La cola está vacía, no hay nada que borrar.")
            else:
                borrado = cola.pop(0)
                print("Se sacó el primer elemento de la cola:", borrado)
        elif opcion == 3:
            if len(cola) == 0:
                print("La cola está vacía.")
            else:
                print("Elementos de la cola (el primero está a la izquierda):")
                for elemento in cola:
                    print(elemento, end=" ")
                print()
        elif opcion == 4:
            print("Saliendo del programa de colas...")
        else:
            print("Opción no válida. Elige del 1 al 4.")
 
    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
