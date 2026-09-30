class PilaPlatosArreglo:
    def __init__(self):
        self.platos = []

    def esta_vacia(self):
        return len(self.platos) == 0

    def apilar(self, plato):
        self.platos.append(plato)
        print(f"[Arreglo] Plato colocado encima: {plato}")

    def desapilar(self):
        if self.esta_vacia():
            print("[Arreglo] Error: No hay platos que retirar.")
            return None
        plato_retirado = self.platos.pop()
        print(f"[Arreglo] Plato retirado del tope: {plato_retirado}")
        return plato_retirado

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.platos[-1]

    def mostrar(self):
        print("\n--- Pila de Platos (Implementación: Arreglo) ---")
        if self.esta_vacia():
            print("   [Pila vacía]")
        else:
            # Imprimimos desde el último (tope) hacia el primero (base)
            for plato in reversed(self.platos):
                print(f"   | {plato.center(20)} |")
            print("   +----------------------+ (Base)")
        print("------------------------------------------------\n")


# SOLUCIÓN 2: Implementación con Lista Enlazada (Nodos y Puntero Tope)
class NodoPlato:
    def __init__(self, tipo_plato):
        self.tipo_plato = tipo_plato
        self.siguiente = None  # Apunta al plato que queda debajo


class PilaPlatosEnlazada:
    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        return self.tope is None

    def apilar(self, plato):
        nuevo_nodo = NodoPlato(plato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        print(f"[Enlazada] Plato colocado encima: {plato}")

    def desapilar(self):
        if self.esta_vacia():
            print("[Enlazada] Error: No hay platos que retirar.")
            return None
        plato_retirado = self.tope.tipo_plato
        self.tope = self.tope.siguiente
        print(f"[Enlazada] Plato retirado del tope: {plato_retirado}")
        return plato_retirado

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.tope.tipo_plato

    def mostrar(self):
        print("\n--- Pila de Platos (Implementación: Lista Enlazada) ---")
        if self.esta_vacia():
            print("   [Pila vacía]")
        else:
            actual = self.tope
            while actual:
                print(f"   | {actual.tipo_plato.center(20)} |")
                actual = actual.siguiente
            print("   +----------------------+ (Base)")
        print("-------------------------------------------------------\n")


# COMPARACIÓN Y DEMOSTRACIÓN DE AMBAS SOLUCIONES
def probar_implementacion(nombre, pila):
    print(f"\n{'='*55}")
    print(f" PRUEBA: {nombre.upper()}")
    print(f"{'='*55}")

    # 1. Agregar platos
    pila.apilar("Plato Base #1")
    pila.apilar("Plato Hondo #2")
    pila.apilar("Plato Postre #3")

    # 2. Ver visualmente cómo quedaron apilados
    pila.mostrar()

    # 3. Consultar el tope sin sacarlo
    print(f"-> Plato actualmente arriba: {pila.ver_tope()}\n")

    # 4. Retirar el último plato colocado (LIFO)
    pila.desapilar()

    # 5. Mostrar cómo queda la pila tras retirar uno
    pila.mostrar()


if __name__ == "__main__":
    # Solución 1: Arreglo
    pila_arreglo = PilaPlatosArreglo()
    probar_implementacion("Solución 1 - Arreglo Dinámico", pila_arreglo)

    # Solución 2: Lista Enlazada
    pila_enlazada = PilaPlatosEnlazada()
    probar_implementacion("Solución 2 - Lista Enlazada", pila_enlazada)