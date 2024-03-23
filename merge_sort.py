# Algoritmo: Merge-Sort

class MergeSort:
    def __init__(self, arr):
        self.counter = 0
        self.arr = arr

    def get_counter(self):
        return self.counter

    def do_merge(self, start, middle, end):

        # Se ajustan los apuntadores de la siguiente forma

        # El apuntador izquierdo sera igual al indice de start
        left = start
        # El apuntador derecho sera igual al indice de middle +1
        right = middle + 1
        # El apuntador final sera igual al indice final +1
        # Esto es para que se pueda recorrer la sublista desde principio a fin, incluyendo su último elemento
        end += 1
        # El apuntador middle seria igual al indice middle + 1
        # Esto es para que se considere dentro de los elementos de la sublista el elemento del medio
        middle += 1

        # Se crea una lista auxiliar que servira para
        # almacenar la sublista en el paso de merger
        aux_lista = []

        while left < middle and right < end:
            self.counter += 1
            if self.arr[left] < self.arr[right]:
                aux_lista.append(self.arr[left])
                left += 1
            elif self.arr[right] < self.arr[left]:
                aux_lista.append(self.arr[right])
                right += 1
            else:
                # Si llegaran a haber dos elementos iguales, se puede escoger
                # uno de los dos elementos para insertarlo primero en la sublista
                # si faltara agregarlo porque el apuntador de la derecha ya no es menor al apuntador final
                # la lógica de los ciclos lo agregara
                aux_lista.append(self.arr[right])
                right += 1

        # Si uno de los apuntadores(izquierdo o derecho) le sobro elementos
        # para colocar dentro de la sublista, se hacen estos ciclos para agregarlos
        # mientras no fallen en cumplir la condición del ciclo

        while left != middle:
            self.counter += 1
            aux_lista.append(self.arr[left])
            left += 1

        while right != end:
            self.counter += 1
            aux_lista.append(self.arr[right])
            right += 1

        # Por último, se va a colocar los elementos de la sublista en la lista real desde la posición
        # start hasta la posición end y puesto que dentro de esa rango hay la misma cantidad de elementos
        # en la posición, los elementos de la lista original asociados a ese rango de indices seran cambiados por
        # los elementos de la sublista.

        if len(aux_lista) > 0:
            aux_index = start
            for element in aux_lista:
                self.counter += 1
                self.arr[aux_index] = element
                aux_index += 1

    def sort(self):
        self.counter = 0
        self.merge_sorting(0, len(self.arr) - 1)

    def merge_sorting(self, start, end):
        if start != end:
            # Se debe usar el doble back-slash para indicar una división de enteros
            middle = (start + end) // 2
            self.counter += 1
            # Se aplica la función merge_sort a la izquierda
            self.merge_sorting(start, middle)
            self.counter += 1
            # Se aplica la función merge a la derecha
            self.merge_sorting(middle + 1, end)
            self.counter += 1

            self.do_merge(start, middle, end)





