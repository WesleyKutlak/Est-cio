meu_dicionario = {
    1: 'Python',
    2: 'Java',
    3: 'PHP'
}

#Imprimir o conteúdo do dicionário
print("Conteúdo do dicionário:", meu_dicionario)

#Imprimir o tipo de dados do dicionário
print("Tipo de dados do dicionário:", type(meu_dicionario))

#método get, imprimir o valor da chave linguagem (Exemplo para chave 1)
print("Valor da chave 1:", meu_dicionario.get(1))

#Imprimir o tamanho do dicionário
print("Tamanho do dicionário:", len(meu_dicionario))

#Criar um novo dicionário aninhado dicionario_frutas
dicionario_frutas = dict({
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
})

#Imprimir o valor das chaves nome e tipo da chave 1
fruta_chave_1 = dicionario_frutas[1]
print("Fruta da chave 1 - Nome:", fruta_chave_1['nome'])
print("Fruta da chave 1 - Tipo:", fruta_chave_1['tipo'])

#Imprimir o valor das chaves nome e tipo da chave 2
fruta_chave_2 = dicionario_frutas[2]
print("Fruta da chave 2 - Nome:", fruta_chave_2['nome'])
print("Fruta da chave 2 - Tipo:", fruta_chave_2['tipo'])

#dicionario_frutas e imprimir os valores de todas as chaves nome e tipo
for chave, fruta in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {fruta['nome']}, Tipo: {fruta['tipo']}")