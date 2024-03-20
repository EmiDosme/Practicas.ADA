import random
import time

def partition(arreglo, low, high):
    pivote = arreglo[high]
    i = low - 1

    for j in range(low, high):
        if arreglo[j] < pivote:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]

    arreglo[i + 1], arreglo[high] = arreglo[high], arreglo[i + 1]
    return i + 1

def quick_sort(arreglo, low, high):
    if low < high:
        pi = partition(arreglo, low, high)
        quick_sort(arreglo, low, pi - 1)
        quick_sort(arreglo, pi + 1, high)

n = int(input("Ingrese el tamaño del arreglo: "))
arr = [random.randint(1, 1000) for _ in range(n)]
print("\nOriginal Array:", arr)

start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)
end_time = time.time() - start_time

print("\nArreglo ordenado con Quicksort:", arr)
print("\nTiempo de ejecución:", end_time, "segundos")
