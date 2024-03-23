class QuickSort:
    """Clase que implementa el algoritmo de ordenamiento Quick Sort.

    Atributos:
        contador (int): Contador de pasos.
        lista (list): Lista a ordenar.

    Métodos:
        obtener_contador(): Retorna el contador de pasos.
        quick_sort(inicio, fin): Ordena la lista utilizando el algoritmo Quick Sort.
        particion(inicio, fin): Realiza la partición de la lista.
        quick_sort_wrapper(): Envoltura para iniciar el proceso de ordenamiento Quick Sort.
    """

    def __init__(self, lista):
        self.contador = 0
        self.lista = lista

    """Retorna el contador de pasos del algoritmo de ordenamiento Quick Sort."""
    def get_counter(self):
        return self.contador

    """Ordena la lista utilizando el algoritmo Quick Sort."""
    def quick_sort(self, inicio, fin):
        if inicio < fin:
            indice_pivote, i = self.particion(inicio, fin)
            self.quick_sort(inicio, indice_pivote - 1)
            self.quick_sort(indice_pivote + 1, fin)
    """Realiza la partición de la lista."""
    def particion(self, inicio, fin):
        pivote = self.lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if self.lista[j] <= pivote:
                i += 1
                self.lista[i], self.lista[j] = self.lista[j], self.lista[i]
                self.contador += 1
        self.lista[i + 1], self.lista[fin] = self.lista[fin], self.lista[i + 1]
        self.contador += 1
        return i + 1, i

    """Envoltura para iniciar el proceso de ordenamiento Quick Sort."""
    def sort(self):
        self.quick_sort(0, len(self.lista) - 1)
