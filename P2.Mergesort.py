import random
import time

def merge_sort(arreglo):
    if len(arreglo) > 1:
        mid = len(arreglo) // 2
        L = arreglo[:mid]
        R = arreglo[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arreglo[k] = L[i]
                i += 1
            else:
                arreglo[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arreglo[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arreglo[k] = R[j]
            j += 1
            k += 1


n = int(input("Ingrese el tamaño del array: "))
arreglo = [random.randint(1, 1000) for _ in range(n)]
print("\nArray Original:", arreglo)

start_time = time.time()
merge_sort(arreglo)
end_time = time.time() - start_time

print("\nArreglo ordenado: ", arreglo)
print("\nTiempo de ejecución:", end_time, "segundos")
