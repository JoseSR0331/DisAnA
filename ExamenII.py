def generar_espiral(n):
    # Inicializar una matriz de tamaño n x n con ceros
    matriz = [[0] * n for _ in range(n)]
    # Definir las direcciones (derecha, abajo, izquierda, arriba)
    direccion = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    fila, columna = 0, 0
    direccion_actual = 0
    # Llenar la matriz con números en un patrón espiral
    for i in range(1, n**2 + 1):
        matriz[fila][columna] = i
        siguiente_fila = fila + direccion[direccion_actual][0]
        siguiente_columna = columna + direccion[direccion_actual][1]
        # Verificar límites y si la siguiente celda está vacía
        if 0 <= siguiente_fila < n and 0 <= siguiente_columna < n and matriz[siguiente_fila][siguiente_columna] == 0:
            fila, columna = siguiente_fila, siguiente_columna
        else:
            # Cambiar de dirección si se alcanza un límite o una celda ocupada
            direccion_actual = (direccion_actual + 1) % 4
            fila += direccion[direccion_actual][0]
            columna += direccion[direccion_actual][1]
    return matriz

def imprimir_matriz(matriz):
    # Imprimir la matriz en formato tabular
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

def main():
    try:
        # Solicitar al usuario un número entero para generar la espiral cuadrada
        numero = int(input("Ingrese un número entero para generar la espiral cuadrada: "))
        if numero < 1:
            raise ValueError("El número debe ser mayor o igual a 1.")
        espiral = generar_espiral(numero)
        print("La espiral cuadrada del número ingresado es:")
        imprimir_matriz(espiral)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()