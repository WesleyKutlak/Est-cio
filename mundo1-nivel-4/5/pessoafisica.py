from pessoa import pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataNascimento, cpf, rg):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__rg = rg

    # getters e setters
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 14:
            raise ValueError("O CPF deve conter 14 caracters (no format 000.000.000-00)")
        else:
           self.__cpf = cpf
    
    @property
    def rg(self):
        return self.rg
    
    @rg.setter
    def rg(self, rg):
        self.__rg = rg
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()  # Imprime informações da classe Pessoa
        print(f"Data de Nascimento: {self.__dataNascimento}")
        print(f"CPF: {self.__cpf}")
        print(f"RG: {self.__rg}")