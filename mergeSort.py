def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamada recursiva para cada mitad
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Mezclar las mitades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    # Comparar los elementos de las dos mitades y combinar en orden
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Añadir los elementos restantes de la mitad izquierda (si los hay)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Añadir los elementos restantes de la mitad derecha (si los hay)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Solicitar al usuario que ingrese los datos
try:
    user_input = input("Introduce una lista de números separados por comas: ")
    # Convertir la entrada del usuario en una lista de enteros
    arr = list(map(int, user_input.split(',')))

    # Ordenar la lista usando el algoritmo Merge Sort
    sorted_arr = merge_sort(arr)

    print("Arreglo ordenado:", sorted_arr)
except ValueError:
    print("Por favor, introduce solo números separados por comas.")
