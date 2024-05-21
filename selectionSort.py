def selection_sort(arr):
    n = len(arr)
    # Recorremos el arreglo
    for i in range(n):
        # Encontrar el índice del menor elemento en el resto del arreglo
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el menor elemento encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Solicitar al usuario que ingrese los datos
try:
    user_input = input("Introduce una lista de números separados por comas: ")
    # Convertir la entrada del usuario en una lista de enteros
    arr = list(map(int, user_input.split(',')))

    # Ordenar la lista usando el algoritmo de ordenamiento por Selección
    sorted_arr = selection_sort(arr)

    print("Arreglo ordenado:", sorted_arr)
except ValueError:
    print("Por favor, introduce solo números separados por comas.")
