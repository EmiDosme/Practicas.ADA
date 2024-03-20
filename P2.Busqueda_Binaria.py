import random
import time

def busqueda_binaria(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

n = int(input("Ingrese el tamaño del arreglo: "))
arr = [random.randint(1, 100) for _ in range(n)]
arr.sort()
x = int(input("Ingrese el valor a buscar (1-100): "))

start_time = time.time()
result = busqueda_binaria(arr, x)
end_time = time.time() - start_time

print("\nArreglo:", arr)

if result != -1:
    print(f"\nEl elemento {x} está presente en el índice", result)
else:
    print("\nEl elemento no está presente")

print("\nTiempo de ejecución:", end_time, "segundos")
