from operacoes import calcular_media, verificar_reprovacao, formatar_dados_reprovado

# Estrutura para armazenar dados dos alunos
alunos = [
    {"nome": "Maria", "matricula": "26", "notas": [8, 7, 5, 9]},
    {"nome": "Ana", "matricula": "101", "notas": [9, 9, 8, 9]},
    {"nome": "Joao", "matricula": "13", "notas": [6, 5, 5, 5]},
    {"nome": "Aghata", "matricula": "37", "notas": [8, 6, 7.5, 9]},
    {"nome": "Joaquim", "matricula": "72", "notas": [6, 5.5, 5, 7]},
    {"nome": "Felix", "matricula": "5", "notas": [10, 8, 8, 8]},
]

# Lista para armazenar dados dos alunos reprovados
alunos_reprovados = []

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    if verificar_reprovacao(media):
        aluno_reprovado_info = formatar_dados_reprovado(aluno["nome"], aluno["matricula"], media)
        alunos_reprovados.append(aluno_reprovado_info)

# Imprimir dados dos alunos reprovados
for info in alunos_reprovados:
    print(info)