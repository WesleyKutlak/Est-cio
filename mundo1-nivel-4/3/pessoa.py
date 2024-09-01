class Pessoa:
    def __init__(self, nome, dataNascimento, cpf, rg):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.rg = rg
        self.status = False

    def alterarStatus(self, status):
        self.status = status