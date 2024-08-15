
def calcular_media(notas):
    """
    Calcula a média das notas fornecidas.
    :param notas: Lista com as notas dos 4 bimestres.
    :return: Média das notas.
    """
    if len(notas) != 4:
        raise ValueError("A lista de notas deve conter exatamente 4 elementos.")
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """
    Verifica se o aluno foi reprovado com base na média.
    :param media: Média final do aluno.
    :return: True se o aluno foi reprovado, False caso contrário.
    """
    return media < 6

def formatar_dados_reprovado(nome, matricula, media):
    """
    Formata os dados do aluno reprovado em uma string.
    :param nome: Nome do aluno.
    :param matricula: Matrícula do aluno.
    :param media: Média final do aluno.
    :return: String formatada com as informações do aluno reprovado.
    """
    return f'Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media:.2f}'
