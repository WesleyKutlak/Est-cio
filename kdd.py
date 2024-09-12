import time

# Função de ordenação Bubble Sort
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# Função de ordenação Selection Sort
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

# Ler o conteúdo do arquivo e separar palavras
nome_arquivo = 'loremipsum.txt'

with open(nome_arquivo, 'r') as arquivo:
    palavras = []
    for linha in arquivo:
        palavras.extend(linha.split())

# Função para medir o tempo de execução
def medir_tempo(funcao, array):
    inicio = time.time()
    funcao(array)
    fim = time.time()
    return fim - inicio

# Testar Bubble Sort
palavras_bubble = palavras.copy()
tempo_bubble = medir_tempo(bubbleSort, palavras_bubble)
print("Palavras ordenadas com Bubble Sort:")
print(palavras_bubble)
print(f"Tempo de execução do Bubble Sort: {tempo_bubble:.6f} segundos")

# Testar Selection Sort
palavras_selection = palavras.copy()
tempo_selection = medir_tempo(selectionSort, palavras_selection)
print("\nPalavras ordenadas com Selection Sort:")
print(palavras_selection)
print(f"Tempo de execução do Selection Sort: {tempo_selection:.6f} segundos")

# Testar método nativo sort
palavras_sort = palavras.copy()
tempo_sort = medir_tempo(lambda x: x.sort(), palavras_sort)
print("\nPalavras ordenadas com o método sort do Python:")
print(palavras_sort)
print(f"Tempo de execução do método sort: {tempo_sort:.6f} segundos")

# Escolher o melhor método (opcional, com base nos tempos medidos) e salvar no arquivo
melhor_ordenacao = min(tempo_bubble, tempo_selection, tempo_sort)

# Determinando o melhor método de ordenação para salvar
if melhor_ordenacao == tempo_bubble:
    palavras_bubble.sort()
    palavras_ordenadas = palavras_bubble
elif melhor_ordenacao == tempo_selection:
    palavras_selection.sort()
    palavras_ordenadas = palavras_selection
else:
    palavras_sort.sort()
    palavras_ordenadas = palavras_sort

# Salvando a lista ordenada em um novo arquivo
novo_arquivo = 'palavras_ordenadas.txt'
with open(novo_arquivo, 'w') as arquivo:
    for palavra in palavras_ordenadas:
        arquivo.write(palavra + '\n')

print(f"\nPalavras ordenadas foram salvas em '{novo_arquivo}'.")

