def insertion_sort(arr):
    # Recorremos el arreglo desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover los elementos del arreglo que son mayores que la clave
        # a una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Solicitar al usuario que ingrese los datos
try:
    user_input = input("Introduce una lista de números separados por comas: ")
    # Convertir la entrada del usuario en una lista de enteros
    arr = list(map(int, user_input.split(',')))

    # Ordenar la lista usando el algoritmo de ordenamiento por Inserción
    sorted_arr = insertion_sort(arr)

    print("Arreglo ordenado:", sorted_arr)
except ValueError:
    print("Por favor, introduce solo números separados por comas.")
