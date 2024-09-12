def bubbleSort(array):
    n = len(array)
    # Laço para iterar sobre todos os elementos
    for i in range(n):
        # Laço interno para comparar elementos adjacentes
        for j in range(0, n - i - 1):
            # Verifica se o elemento atual é maior que o próximo
            if array[j] > array[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                array[j], array[j + 1] = array[j + 1], array[j]

# Exemplo de uso do método bubbleSort
if __name__ == "__main__":
    # Criando um array de números inteiros aleatórios
    import random
    array_numeros = [random.randint(1, 100) for _ in range(15)]
    print("Array original de números inteiros:")
    print(array_numeros)

    # Ordenando o array usando bubbleSort
    bubbleSort(array_numeros)
    
    # Imprimindo o array ordenado
    print("\nArray ordenado usando Bubble Sort:")
    print(array_numeros)
