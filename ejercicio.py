class NodoPlato:
    def __init__(self, tipo_plato):
        self.tipo_plato = tipo_plato  
        self.siguiente = None       



class PilaPlatos:
    def __init__(self):
        self.tope = None  

    def esta_vacia(self):
        return self.tope is None

    def apilar(self, tipo_plato):
        nuevo_plato = NodoPlato(tipo_plato)
        nuevo_plato.siguiente = self.tope  
        self.tope = nuevo_plato           
        print(f"Plato agregado: {tipo_plato}")

    def desapilar(self):
        if self.esta_vacia():
            print("No hay platos para retirar. La pila está vacía.")
            return None
        
        plato_retirado = self.tope.tipo_plato
        self.tope = self.tope.siguiente    
        print(f"Plato retirado: {plato_retirado}")
        return plato_retirado

    def ver_tope(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.tope.tipo_plato

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


if __name__ == "__main__":
    pila = PilaPlatos()

    pila.apilar("Plato llano #1")
    pila.apilar("Plato hondo #2")
    pila.apilar("Plato de postre #3")

    pila.mostrar_platos()

    print(f"Plato en el tope actual: {pila.ver_tope()}\n")

    pila.desapilar()
    pila.desapilar()

    pila.mostrar_platos()

    # HolaMundo("print")