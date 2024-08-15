# Criação do dicionário inicial
dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

#Adicionando novos elementos - usando update
dicionario.update({
    2: {'nome': 'Alexandre', 'idade': 25, 'nacionalidade': 'português'},
    3: {'nome': 'Mariana', 'idade': 24, 'nacionalidade': 'brasileira'}
})

#Imprimindo o dicionário atualizado
print("Dicionário atualizado:", dicionario)

#Criando uma cópia do dicionário
copia_dicionario = dicionario.copy()

#Imprimindo a cópia
print("Cópia do dicionário:", copia_dicionario)

#Removendo o elemento com chave 2
elemento_removido = dicionario.pop(2)

#Imprimindo o elemento removido e o dicionário atualizado
print("Elemento removido:", elemento_removido)
print("Dicionário após remoção:", dicionario)

#Removendo o último item com popitem
ultimo_item = dicionario.popitem()

#Imprimindo o item removido e o dicionário atualizado
print("Último item removido:", ultimo_item)
print("Dicionário após remoção do último item:", dicionario)

# Limpando o dicionário usando clear
dicionario.clear()
copia_dicionario.clear()

#Imprimindo os dicionários após a limpeza
print("Dicionário original após clear:", dicionario)
print("Cópia do dicionário após clear:", copia_dicionario)


#Definição e criação de um Novo Dicionário com fromKeys
novas_chaves = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(novas_chaves, 'valor padrão')

#Imprimindo o conteúdo do novo dicionário
print("Novo dicionário:", novo_dicionario)

#Imprimindo as chaves, valores e itens do novo dicionário
print("Itens do novo dicionário:", novo_dicionario.items())
print("Chaves do novo dicionário:", novo_dicionario.keys())
print("Valores do novo dicionário:", novo_dicionario.values())