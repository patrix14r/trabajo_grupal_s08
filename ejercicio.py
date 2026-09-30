# 1. Clase Nodo: representa cada plato individual
class NodoPlato:
    def __init__(self, tipo_plato):
        self.tipo_plato = tipo_plato  # Dato: ej. "Plato hondo", "Plato llano"
        self.siguiente = None         # Enlace al plato que está debajo


# 2. Clase PilaPlatos: administra la pila usando listas enlazadas
class PilaPlatos:
    def __init__(self):
        self.tope = None  # Inicialmente no hay platos en la pila

    def esta_vacia(self):
        return self.tope is None

    # Agregar plato (Push) -> Se coloca encima
    def apilar(self, tipo_plato):
        nuevo_plato = NodoPlato(tipo_plato)
        nuevo_plato.siguiente = self.tope  # El nuevo plato apunta al anterior tope
        self.tope = nuevo_plato            # El nuevo plato pasa a ser el tope
        print(f"Plato agregado: {tipo_plato}")

    # Retirar plato (Pop) -> Principio LIFO: se retira el del tope
    def desapilar(self):
        if self.esta_vacia():
            print("No hay platos para retirar. La pila está vacía.")
            return None
        
        plato_retirado = self.tope.tipo_plato
        self.tope = self.tope.siguiente    # El tope ahora es el plato de abajo
        print(f"Plato retirado: {plato_retirado}")
        return plato_retirado

    # Consultar el plato de arriba (Peek) -> Solo mirar, no retirar
    def ver_tope(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.tope.tipo_plato

    # Mostrar todos los platos de arriba hacia abajo
    def mostrar_platos(self):
        if self.esta_vacia():
            print("Pila vacía: [ ]")
            return
        
        actual = self.tope
        print("\n--- Estado actual de la pila (Tope -> Fondo) ---")
        while actual:
            print(f"| {actual.tipo_plato} |")
            actual = actual.siguiente
        print("------------------------------------------------\n")


# --- Demostración del funcionamiento ---
if __name__ == "__main__":
    pila = PilaPlatos()

    # 1. Agregar platos
    pila.apilar("Plato llano #1")
    pila.apilar("Plato hondo #2")
    pila.apilar("Plato de postre #3")

    # 2. Mostrar la pila completa
    pila.mostrar_platos()

    # 3. Consultar cuál está arriba
    print(f"Plato en el tope actual: {pila.ver_tope()}\n")

    # 4. Retirar platos (sale primero el último que entró)
    pila.desapilar()
    pila.desapilar()

    # 5. Estado final de la pila
    pila.mostrar_platos()