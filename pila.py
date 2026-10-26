# Ejercicio 2. Pilas
repetir = "s"
 
while repetir == "s":
    pila = []
    opcion = 0
 
    while opcion != 4:
        print("\n--- MENÚ PILA ---")
        print("1. Insertar pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")
 
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Escribe solo un número del 1 al 4.")
            opcion = 0
            continue
 
        if opcion == 1:
            try:
                numero = int(input("Escribe el número que quieres agregar: "))
                pila.append(numero)
                print("Número agregado a la pila.")
            except ValueError:
                print("Eso no es un número.")
        elif opcion == 2:
            if len(pila) == 0:
                print("La pila está vacía, no hay nada que quitar.")
            else:
                quitado = pila.pop()
                print("Se quitó el último elemento de la pila:", quitado)
        elif opcion == 3:
            if len(pila) == 0:
                print("La pila está vacía.")
            else:
                print("Elementos de la pila (de arriba hacia abajo):")
                for i in range(len(pila) - 1, -1, -1):
                    print(pila[i])
        elif opcion == 4:
            print("Saliendo del programa de pilas...")
        else:
            print("Opción no válida. Elige del 1 al 4.")
 
    repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ").lower()
