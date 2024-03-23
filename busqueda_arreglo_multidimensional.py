def buscar_valor(matriz, valor):
    """
    Buscar un valor específico en una matriz bidimensional.
    Devuelve True si se encuentra el valor y False si no se encuentra.
    Mostrar la posición del valor si se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                print(f"El valor {valor} se encontró en la posición ({i}, {j}) de la matriz.")
                return True
    print(f"El valor {valor} no se encontró en la matriz.")
    return False

# Definir una matriz de ejemplo (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar en la matriz
valor_a_buscar = 5

# Llamar a la función para buscar el valor
buscar_valor(matriz, valor_a_buscar)
