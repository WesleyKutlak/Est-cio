import random

# Criando um array de 15 números inteiros aleatórios
array_numeros = [random.randint(1, 100) for _ in range(15)]
print("Array original de números inteiros:")
print(array_numeros)

# Ordenando o array em ordem crescente
array_numeros.sort()
print("\nArray ordenado em ordem crescente:")
print(array_numeros)

# Ordenando o array em ordem decrescente
array_numeros.sort(reverse=True)
print("\nArray ordenado em ordem decrescente:")
print(array_numeros)

# Criando um array de strings
array_strings = ["wesley", "11121998", "45645645645", "121211211"]
print("\nArray original de strings:")
print(array_strings)

# Ordenando o array de strings em ordem crescente
array_strings.sort()
print("\nArray de strings ordenado em ordem crescente:")
print(array_strings)

# Ordenando o array de strings em ordem decrescente
array_strings.sort(reverse=True)
print("\nArray de strings ordenado em ordem decrescente:")
print(array_strings)
