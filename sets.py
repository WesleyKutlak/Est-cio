
# Criar uma estrutura de dados do tipo set com o nome de “set_inicial”
set_inicial = {11, 12, 13, 14}

# Imprimir set
print("Conteúdo de set_inicial:", set_inicial)

# Adicionar o elemento 15 ao set
set_inicial.add(15)

# Imprimir o conteúdo do set
print("Conteúdo de set_inicial após adicionar 15:", set_inicial)

# Atualizar set com os elementos 1, 2, 3, 4, 5
set_inicial.update({1, 2, 3, 4, 5})

# Imprimir conteúdo do set
print("Conteúdo de set_inicial após atualização:", set_inicial)

# Remover elemento 13 do set
set_inicial.discard(13)

# Imprimir conteúdo do set
print("Conteúdo de set_inicial após remover 13:", set_inicial)

# Criar novo set chamado “novo_set”
novo_set = {20, 21, 23, 1, 2}

# Imprimir conteúdo do novo set
print("Conteúdo de novo_set:", novo_set)

# Imprimir resultado da união entre os dois sets
uniao = set_inicial.union(novo_set)
print("União entre set_inicial e novo_set:", uniao)

# Imprimir resultado da interseção entre os dois sets
intersecao = set_inicial.intersection(novo_set)
print("Interseção entre set_inicial e novo_set:", intersecao)

# Imprimir resultado da diferença entre os dois sets
diferenca = set_inicial.difference(novo_set)
print("Diferença entre set_inicial e novo_set:", diferenca)

# Imprimir resultado da diferença simétrica entre os dois sets
diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre set_inicial e novo_set:", diferenca_simetrica)
