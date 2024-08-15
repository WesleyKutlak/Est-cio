lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Imprimindo o conteúdo da lista
print("Conteúdo da lista_mesclada:", lista_mesclada)

# Adicionando um elemento à lista usando append
lista_mesclada.append(["Lista aninhada"])

# Imprimindo o conteúdo da lista após o append
print("Conteúdo da lista_mesclada após append:", lista_mesclada)

# Inserindo um elemento na posição 4 usando insert
lista_mesclada.insert(4, 5)

# Imprimindo o conteúdo da lista após o insert
print("Conteúdo da lista_mesclada após insert:", lista_mesclada)

# Imprimindo o tamanho atual da lista
print("Tamanho atual da lista_mesclada:", len(lista_mesclada))

# Removendo o item na posição 1
del lista_mesclada[1]

# Imprimindo o conteúdo da lista após a remoção
print("Conteúdo da lista_mesclada após remoção:", lista_mesclada)

# Criando uma nova lista com os itens até a posição 4 da lista anterior
nova_lista_mesclada = lista_mesclada[:5]

# Imprimindo o conteúdo da nova lista
print("Conteúdo da nova_lista_mesclada:", nova_lista_mesclada)