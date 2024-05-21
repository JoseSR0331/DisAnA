def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Verificar si el hijo izquierdo del nodo raíz existe y es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificar si el hijo derecho del nodo raíz existe y es mayor que la raíz
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Cambiar la raíz, si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapificar la raíz
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar
        heapify(arr, i, 0)

    return arr

# Solicitar al usuario que ingrese los datos
try:
    user_input = input("Introduce una lista de números separados por comas: ")
    # Convertir la entrada del usuario en una lista de enteros
    arr = list(map(int, user_input.split(',')))

    # Ordenar la lista usando el algoritmo Heap Sort
    sorted_arr = heap_sort(arr)

    print("Arreglo ordenado:", sorted_arr)
except ValueError:
    print("Por favor, introduce solo números separados por comas.")
