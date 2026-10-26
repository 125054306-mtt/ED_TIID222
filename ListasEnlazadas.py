#Clase que representa un Nodo
class   Nodo:

    def __init__(self, numero):
        #Estructura de un nodo
        self.numero = numero

        self.siguiente= None

#Clase que vba a daministrar los nodos de las listas enlazadas
class ListEnlazada:

    def __init__(self):

        self.cabeza = None

    #Método para insertar un nodo al inicio de la lista
    def Insertar_Nodo_al_Inicio(self, numero):

        #Crear un nuevo nodo con el numero recibido
        nuevo_nodo = Nodo(numero)

        #Comprobar si la lista está vacía
        if(self.cabeza is None):

            #Vamos a pasar el nuevo Nodo a nuestra cabeza
            self.cabeza = Nodo(numero)

            return
        #Si la lista ya tenía nodos, elk nuevo nodo aspunta al que era la cabeza
        nuevo_nodo.siguiente = self.cabeza

        #Actualizar nuestra cabeza para que apunte al nuevo nodo
        self.cabeza = nuevo_nodo

    #Método para insertar un nodo al final de la lista
    def Insertar_Nodo_al_Final(self, numero):

        #Crear el noddo con el número que se recibe
        nuevo_nodo = Nodo(numero)

        #Comprobar si la lista está vacía
        if(self.cabeza == None):

            #Si la lista está vacía, el nuevo nodo será el primero (Cabeza)
            self.cabeza = nuevo_nodo

            return

        #Referencia temporal al primer nodo
        actual = self.cabeza

        #Avanzar mientras exista un nodo siguiente (Actual.siguiente)
        while(actual.siguiente):

            #Mi actual ahora pasa a ser mi actual.lsiguiente
            actual = actual.siguiente

        #Cuando ya no hay un actual.siguiente es ahi cuando conecta el nuevo nodo
        actual.siguiente = nuevo_nodo

    #Método para imprir nuestra lista enlazada
    def Imprimir_ListaEnlazada(self):

        actual= self.cabeza

        while(actual):

            #Con esta línea ímprimimos nuestra lista sin saltos de línea
            print(actual.numero, "→", end=" ")

            #Avanzamos al siguiente nodo y ahora ese será el actual
            actual = actual.siguiente

        #Sino apunta a None
        print("None")

Mi_lista = ListEnlazada()
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Insertar_Nodo_al_Final(56)
Mi_lista.Imprimir_ListaEnlazada()