import random

def selectionSort(array):
    # Laço externo para iterar sobre todos os elementos
    for i in range(len(array)):
        # Cria uma variável que inicialmente é o índice atual
        min_index = i
        # Laço interno para iterar a partir do próximo elemento até o final do array
        for j in range(i + 1, len(array)):
            # Verifica se o valor no índice atual é maior que o valor no índice j
            if array[j] < array[min_index]:
                # Se sim, atualiza o índice do menor elemento encontrado
                min_index = j
        # Troca os valores no índice atual com o índice do menor elemento encontrado
        array[i], array[min_index] = array[min_index], array[i]

# Criando um array de 15 números inteiros aleatórios
array_numeros = [random.randint(1, 100) for _ in range(15)]
print("Array original de números inteiros:")
print(array_numeros)

# Ordenando o array usando selectionSort
selectionSort(array_numeros)

# Imprimindo o array ordenado
print("\nArray ordenado usando Selection Sort:")
print(array_numeros)
