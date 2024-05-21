def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Solicitar al usuario que ingrese los datos
try:
    user_input = input("Introduce una lista de números separados por comas: ")
    # Convertir la entrada del usuario en una lista de enteros
    arr = list(map(int, user_input.split(',')))

    # Ordenar la lista usando el algoritmo optimizado de ordenamiento Burbuja
    sorted_arr = bubble_sort_optimized(arr)

    print("Arreglo ordenado:", sorted_arr)
except ValueError:
    print("Por favor, introduce solo números separados por comas.")