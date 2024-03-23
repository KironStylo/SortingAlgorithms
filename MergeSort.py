# Algoritmo: Merge-Sort
import time
import matplotlib.pyplot as plt

# Análisis de complejidad algoritmica del algoritmo de ordenamiento Merge Sort

# Notación Big 0: Complejidad de n*log(n)
# El peor caso es que los elementos esten ordenados de forma descendente
lista_o = [i for i in range(100, 0, -1)]

# Notación Big Theta: Complejidad de n*log(n)
# El caso promedio es que mitad de la lista este ordenada descendente y mitad de la lista este ordenada ascendentemente
lista_theta = list(i for i in range(100, 50, -1))
lista_theta.extend(list(i for i in range(1, 50, 1)))

# Notación Big Omega: Complejidad de n*log(n)
# El mejor caso es que la lista este ordenada de forma ascendente
lista_omega = [i for i in range(0, 100, 1)]


# En otras palabras, cualquiera de estos casos nos puede servir para
# hallar la gráfica del número de entradas contra el tiempo y el número
# de pasos contra el tamaño de la lista.

# Análisis de complejidad algoritmica del algoritmo de ordenamiento Quick Sort


# Se crea un dictionario que almacene para cada algoritmo:
# Datos del peor escenario que corresponde a los:
# inputs (Datos de entrada)
# time (tiempo para ordenar los datos de entrada)
# steps (cantidad de pasos que requiere el algoritmo)
def create_dictionary():
    algorithms = {
        'merge':
            {
                'worst-case': {
                    'inputs': [],
                    'time': [],
                    'steps': []
                }
            },
        'quick': {
            'worst-case': {
                'inputs': [],
                'time': [],
                'steps': []
            }
        }
    }
    return algorithms


def measure_time_and_steps(arr):
    ms = MergeSort(arr)
    start = time.perf_counter()
    ms.merge_sort()
    end = time.perf_counter()
    return end - start, ms.get_counter()


# Casos de uso de merge peor_caso
def merge_worst_use_cases():
    # Tamaño de la lista
    lists = []
    for i in range(100, 10000, 10):
        one_list = []
        for j in range(i, 0, -1):
            one_list.append(j)
        lists.append(one_list)
    return lists


def fill_merge_algortihm_worst_case(algorithm: dict):
    cases = algorithm['merge']['worst-case']
    # Primero se llenan los inputs
    data = merge_worst_use_cases()
    cases['inputs'] = list(len(i) for i in data)

    # Lista de tiempos de ordenamiento para cada entrada
    tiempos_ordenamiento = []
    # Lista de pasos para ordenar para cada entrada
    pasos_ordenamiento = []

    # Segundo se calcula el tiempo que toma Merge en ordenar y el número de pasos:
    for i in range(0, len(data)):
        algo_time, algo_steps = measure_time_and_steps(data[i])
        tiempos_ordenamiento.append(algo_time)
        pasos_ordenamiento.append(algo_steps)

    # Llenar el dicionario con los tiempos de ordenamiento y pasos
    cases['time'] = tiempos_ordenamiento
    cases['steps'] = pasos_ordenamiento


def plot_merge_results(algo_dic):
    merge = algo_dic["merge"]
    merge_worst = merge["worst-case"]
    merge_worst_input = merge_worst["inputs"]
    merge_worst_time = merge_worst["time"]
    merge_worst_steps = merge_worst["steps"]

    plt.plot(merge_worst_input, merge_worst_time, label="Merge_Sort")
    plt.xlabel('Tamaño de la lista')
    plt.title("Comparación peor caso para Merge Sort y Quick Sort")
    plt.ylabel('Tiempo (s)')
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(merge_worst_input, merge_worst_steps, label="Merge_Sort")
    plt.xlabel('Tamaño de la lista')
    plt.title("Comparación peor caso para Merge Sort y Quick Sort")
    plt.ylabel('Pasos (n)')
    plt.legend()
    plt.grid()
    plt.show()


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

    def merge_sort(self):
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


algo_dict = create_dictionary()
fill_merge_algortihm_worst_case(algo_dict)
plot_merge_results(algo_dict)
