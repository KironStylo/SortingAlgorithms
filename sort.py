import time
import os
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial
from merge_sort import MergeSort
from quick_sort import QuickSort

algoritmos_final = {}

def main():
    analisis_algoritmos()
    # Calcular el modelo de regresión polinomial para Quick Sort
    calculate_polynomial_regression_quick_sort('peor-caso')
    calculate_polynomial_regression_quick_sort('caso-promedio')
    calculate_polynomial_regression_quick_sort('mejor-caso')

    print("\n")

    # Calcular el modelo de regresión lineal para Merge Sort
    calculate_linear_regression_merge_sort_space('peor-caso')
    calculate_linear_regression_merge_sort_space('caso-promedio')
    calculate_linear_regression_merge_sort_space('mejor-caso')

def create_dictionary():
    algoritmos = {
        'merge': {
            'mejor-caso': {
                'lista-entrada': [], 
                'tiempo': [], 
                'pasos': []
            },
            'caso-promedio': {
                'lista-entrada': [], 
                'tiempo': [], 
                'pasos': []
            },
            'peor-caso': {
                'lista-entrada': [], 
                'tiempo': [], 
                'pasos': []
            }
        },
        'quick': {
            'mejor-caso': {
                'lista-entrada': [], 
                'tiempo': [], 
                'pasos': []
            },
            'caso-promedio': {
                'lista-entrada': [], 
                'tiempo': [], 
                'pasos': []
            },
            'peor-caso': {
                'lista-entrada': [], 
                'tiempo': [], 
                'pasos': []
            }
        }
    }
    return algoritmos


def analisis_algoritmos():
    global algoritmos_final
    algoritmos = create_dictionary()

    # Merge Sort
    fill_algorithm_cases(algoritmos, 'merge')

    # Quick Sort
    
    fill_algorithm_cases(algoritmos, 'quick')
    algoritmos_final = algoritmos
    plot_results(algoritmos)
    plot_comparison(algoritmos)

def fill_algorithm_cases(algoritmos, algorithm):
    if algorithm == 'merge':
        sorting_class = MergeSort
    elif algorithm == 'quick':
        sorting_class = QuickSort

    for case in ['peor-caso', 'caso-promedio', 'mejor-caso']:
        data =  [[j for j in range(1, i + 1)] for i in range(10, 1000, 10)]  # Listas ordenadas de 10 a 1000 elementos
        algoritmos[algorithm][case]['lista-entrada'] = list(len(i) for i in data)
        times = []
        steps = []
        for i in range(0, len(data)):
            if algorithm == 'merge':
                #Si es caso-promedio entonces la lista es aleatoria
                if(case == 'caso-promedio'):
                    random.shuffle(data[i])
                #Si es mejor-caso entonces la lista esta ordenada
                elif((case == 'mejor-caso')):
                    data[i].sort()
                #Si es peor-caso entonces la lista esta en orden descendente
                elif((case == 'peor-caso')):
                    data[i].sort(reverse=True)
            else:
                #Si es caso-promedio entonces la lista es aleatoria
                if(case == 'caso-promedio'):
                    random.shuffle(data[i])
                #Si es mejor-caso entonces la lista esta parcialmente ordenada
                elif((case == 'mejor-caso')):
                    data[i].sort()
                    data[i] = generate_best_case_lists(data[i])
                #Si es peor-caso entonces la lista esta ordenada en orden ascendente o descendente 
                elif((case == 'peor-caso')):
                    data[i].sort()
            time, step = measure_time_and_steps(data[i], sorting_class)
            times.append(time)
            steps.append(step)
        algoritmos[algorithm][case]['tiempo'] = times
        algoritmos[algorithm][case]['pasos'] = steps

def generate_best_case_lists(lista):
    n = len(lista)
    # Desordenar algunos elementos
    for _ in range(n // 10):  # Desordenar aproximadamente el 10% de los elementos
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        lista[i], lista[j] = lista[j], lista[i]
    
    return lista


def generate_worst_case_lists():
    lists = []
    for i in range(100, 10000, 10):
        one_list = []
        for j in range(i, 0, -1):
            one_list.append(j)
        lists.append(one_list)
    return lists

def measure_time_and_steps(arr, sorting_class):
    sorting_instance = sorting_class(arr)
    start = time.perf_counter()
    sorting_instance.sort()
    end = time.perf_counter()
    return end - start, sorting_instance.get_counter()

def plot_results(algoritmos):
    # Gráfica para tiempo de ejecución
    for algorithm in algoritmos:
        plt.figure()  # Crear una nueva figura para cada algoritmo
        for case in ['mejor-caso', 'caso-promedio', 'peor-caso']:
            plt.plot(algoritmos[algorithm][case]['lista-entrada'],
                     algoritmos[algorithm][case]['tiempo'],
                     label=f"{algorithm.capitalize()} {case.replace('-', ' ').capitalize()}")
        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Tiempo (s)')
        plt.title(f"Comparación de casos para {algorithm.capitalize()} Sort")
        plt.legend()
        plt.grid()
        # Ruta de la carpeta donde se guardará la imagen
        carpeta = 'complejidad_' + algorithm
    
        # Verificar si la carpeta existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)  # Crear la carpeta si no existe
        plt.savefig(f'{carpeta}/{algorithm}_tiempo_comparacion.png')  # Guardar como PNG
        plt.close()  # Cerrar la figura actual

    # Gráfica para número de pasos
    for algorithm in algoritmos:
        plt.figure()  # Crear una nueva figura para cada algoritmo
        for case in ['mejor-caso', 'caso-promedio', 'peor-caso']:
            plt.plot(algoritmos[algorithm][case]['lista-entrada'],
                     algoritmos[algorithm][case]['pasos'],
                     label=f"{algorithm.capitalize()} {case.replace('-', ' ').capitalize()}")
        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Pasos (n)')
        plt.title(f"Comparación de casos para {algorithm.capitalize()} Sort")
        plt.legend()
        plt.grid()

        # Ruta de la carpeta donde se guardará la imagen
        carpeta = 'complejidad_' + algorithm
    
        # Verificar si la carpeta existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)  # Crear la carpeta si no existe

        plt.savefig(f'{carpeta}/{algorithm}_pasos_comparacion.png')  # Guardar como PNG
        plt.close()  # Cerrar la figura actual

def plot_comparison(algoritmos):
    # Gráfica para tiempo de ejecución
    for case in ['mejor-caso', 'caso-promedio', 'peor-caso']:
        plt.figure()  # Crear una nueva figura para cada caso
        for algorithm in algoritmos:
            plt.plot(algoritmos[algorithm][case]['lista-entrada'],
                     algoritmos[algorithm][case]['tiempo'],
                     label=f"{algorithm.capitalize()} {case.replace('-', ' ').capitalize()}")
        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Tiempo (s)')
        plt.title(f"Comparación de algoritmos para {case.replace('-', ' ').capitalize()}")
        plt.legend()
        plt.grid()
        # Ruta de la carpeta donde se guardará la imagen
        carpeta = 'comparacion_complejidad_temporal'
    
        # Verificar si la carpeta existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)  # Crear la carpeta si no existe
        plt.savefig(f'{carpeta}/comparacion_{case}_tiempo.png')  # Guardar como PNG
        plt.close()  # Cerrar la figura actual

    # Gráfica para número de pasos
    for case in ['mejor-caso', 'caso-promedio', 'peor-caso']:
        plt.figure()  # Crear una nueva figura para cada caso
        for algorithm in algoritmos:
            plt.plot(algoritmos[algorithm][case]['lista-entrada'],
                     algoritmos[algorithm][case]['pasos'],
                     label=f"{algorithm.capitalize()} {case.replace('-', ' ').capitalize()}")
        plt.xlabel('Tamaño de la lista')
        plt.ylabel('Pasos (n)')
        plt.title(f"Comparación de algoritmos para {case.replace('-', ' ').capitalize()}")
        plt.legend()
        plt.grid()
        # Ruta de la carpeta donde se guardará la imagen
        carpeta = 'comparacion_complejidad_espacial'
    
        # Verificar si la carpeta existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)  # Crear la carpeta si no existe
        plt.savefig(f'{carpeta}/comparacion_{case}_pasos.png')  # Guardar como PNG
        plt.close()  # Cerrar la figura actual

def calculate_polynomial_regression_quick_sort(caso):
    global algoritmos_final
    
    # Obtener los datos de entrada y pasos para Quick Sort
    x = np.array(algoritmos_final['quick'][caso]['lista-entrada'])
    y = np.array(algoritmos_final['quick'][caso]['pasos'])

    # Aplicar logaritmo a los datos de entrada
    log_x = np.log(x)

    # Ajustar un modelo polinómico a los datos transformados
    coef = np.polyfit(log_x, y, 1)

    print("Algoritmo Quick Sort -", caso.replace('-', ' ').capitalize())
    # Imprimir los coeficientes
    print("Coeficientes del polinomio: ", coef)

    # Crear un polinomio a partir de los coeficientes
    poly = np.poly1d(coef)

    # Imprimir la ecuación de la función
    print("Ecuación de la función: y = {:.2f} log(x) + {:.2f}".format(coef[0], coef[1]))

    return poly

def calculate_linear_regression_merge_sort_space(caso):
    global algoritmos_final
     # Obtener los datos de entrada y pasos para Merge Sort
    x = np.array(algoritmos_final['merge'][caso]['lista-entrada'])
    y = np.array(algoritmos_final['merge'][caso]['pasos'])

    # Ajustar un modelo lineal a los datos
    coef = np.polyfit(x, y, 1)

    print("Algoritmo Merge Sort -", caso.replace('-', ' ').capitalize())
    # Imprimir los coeficientes
    print("Coeficientes del polinomio: ", coef)

    # Crear un polinomio a partir de los coeficientes
    poly = np.poly1d(coef)

    # Imprimir la ecuación de la función
    print("Ecuación de la función: y = {:.2f}x + {:.2f}".format(coef[0], coef[1]))

    return poly

if __name__ == '__main__':
    main()


"""
Quick Sort
Peor Caso: En el peor caso, Quick Sort puede degradarse a una complejidad cuadrática O(n^2) si el pivote elegido 
es el menor o mayor elemento de la lista. En este caso, el algoritmo no divide la lista en dos sublistas de tamaño similar, 
sino que una de las sublistas es vacía y la otra contiene todos los elementos menos el pivote. Esto ocurre cuando la lista 
está ordenada en orden ascendente o descendente.

Mejor Caso: En el mejor caso, Quick Sort tiene una complejidad de O(n log n).  Esto ocurre cuando el pivote elegido divide la 
lista en dos subconjuntos de tamaño aproximadamente igual en cada paso. Esto sucede cuando la lista está desordenada.

Caso Promedio: En el caso promedio, Quick Sort tiene una complejidad de O(n log n). , que es igual al mejor caso. Esto se debe 
a que la elección aleatoria de pivotes en la implementación estándar tiende a producir divisiones equilibradas.

La complejidad espacial del algoritmo Quick Sort es O(n log n) para el peor caso y el mejor caso. Esto se debe a la recursión que 
ocurre en la pila de llamadas. Sin embargo, en el peor caso, puede alcanzar O(n) debido a la profundidad máxima de la recursión 
cuando la partición siempre divide la lista en un subconjunto de tamaño 0 y otro de tamaño n−1.


Merge Sort
Peor Caso: En el peor caso, Merge Sort tiene una complejidad de O(n log n), tanto en el peor caso como en el mejor caso. 
Esto se debe a su naturaleza dividir-y-conquistar, donde siempre divide la lista a la mitad y luego combina las sublistas ordenadas.

Mejor Caso: Al igual que en el peor caso, el mejor caso de Merge Sort también tiene una complejidad de tiempo de O(n log n), 
ya que siempre divide la lista a la mitad y luego combina las sublistas ordenadas.

Caso Promedio: Merge Sort tiene una complejidad de tiempo de O(n log n) en el caso promedio, lo que es igual a su complejidad 
en el peor caso y el mejor caso. Esto se debe a que no depende del estado de la lista de entrada.

Complejidad Espacial:
La complejidad espacial de Merge Sort es O(n) debido al espacio adicional requerido para almacenar las sublistas durante la 
fase de fusión. Esto significa que puede ser menos eficiente en términos de memoria en comparación con Quick Sort, especialmente 
para listas muy grandes.
"""