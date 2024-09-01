from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataAberturaEmpresa, cnpj):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataAberturaEmpresa = dataAberturaEmpresa
        self.__cnpj = cnpj

    #getters e setters
    @property
    def dataAberturaEmpresa(self):
        return self.__dataAberturaEmpresa

    @dataAberturaEmpresa.setter
    def dataAberturaEmpresa(self, dataAberturaEmpresa):
        self.__dataAberturaEmpresa = dataAberturaEmpresa

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        print(len(cnpj))
        if len(cnpj) != 18:
            raise ValueError("O CNPJ deve conter 18 caracters (no format 00.000.000/0001-00)")  
        self.__cnpj = cnpj

    def imprimir_informacoes(self):
        super().imprimir_informacoes()  # Imprime informações da classe Pessoa
        print(f"Data de Abertura da Empresa: {self.__dataAberturaEmpresa}")
        print(f"CNPJ: {self.__cnpj}")
    