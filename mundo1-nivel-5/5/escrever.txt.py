# Nome do arquivo de texto
nome_arquivo = 'texto.txt'

# Criando e abrindo o arquivo para escrita
with open(nome_arquivo, 'w') as arquivo:
    # Criando uma lista e adicionando algumas frases
    texto = list()
    texto.append("Esta é a primeira frase.")
    texto.append("Aqui está a segunda frase.")
    texto.append("E esta é a terceira frase.")
    
    # Escrevendo o conteúdo da lista no arquivo
    for frase in texto:
        arquivo.write(frase + '\n')  # Adiciona uma nova linha após cada frase

print(f"O conteúdo da lista foi escrito no arquivo '{nome_arquivo}'.")
