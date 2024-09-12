# Nome do arquivo de texto
nome_arquivo = 'loremipsum.txt'

# Atribuindo o conteúdo do arquivo à variável e imprimindo
arquivo = open(nome_arquivo, 'r')
conteudo = arquivo.read()
print("Conteúdo completo do arquivo:")
print(conteudo)
arquivo.close()

# Imprimindo apenas a primeira linha do arquivo
arquivo = open(nome_arquivo, 'r')
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha.strip())  # strip() remove espaços em branco no final da linha
arquivo.close()

# Imprimindo os 3 primeiros caracteres do arquivo
arquivo = open(nome_arquivo, 'r')
primeiros_caracteres = arquivo.read(3)
print("\n3 primeiros caracteres do arquivo:")
print(primeiros_caracteres)
arquivo.close()

# Usando a instrução `with` para abrir o arquivo, armazenar seu conteúdo e imprimir
with open(nome_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print("\nConteúdo completo do arquivo com a instrução 'with':")
    print(conteudo)
