import random
import time

def ternary_search(arreglo, left, right, x):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arreglo[mid1] == x:
            return mid1
        if arreglo[mid2] == x:
            return mid2

        if arreglo[mid1] > x:
            return ternary_search(arreglo, left, mid1 - 1, x)
        elif arreglo[mid2] < x:
            return ternary_search(arreglo, mid2 + 1, right, x)
        else:
            return ternary_search(arreglo, mid1 + 1, mid2 - 1, x)

    return -1

n = int(input("Ingrese el tamaño del arreglo: "))
arr = [random.randint(1, 100) for _ in range(n)]
arr.sort()
x = int(input("Ingrese el valor a buscar(1-100): "))

start_time = time.time()
result = ternary_search(arr, 0, n - 1, x)
end_time = time.time() - start_time

print("\nArreglo creado:", arr)

if result != -1:
    print(f"\nEl elemento {x} está presente en el índice {result}")
else:
    print("\nEl elemento no está presente en el arreglo")

print("\nTiempo de ejecución:", end_time, "segundos")
