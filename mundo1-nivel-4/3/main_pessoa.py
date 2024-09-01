from Pessoa import Pessoa

#instancia da classe Pessoa
pessoa_ins = Pessoa("Joao", "2000-01-01", "000.111.222-33", "15975388-1")

attrs = vars(pessoa_ins)

print("Instancia da classe Pessoa: ")
print(', '.join("%s: %s" % item for item in attrs.items()))

pessoa_ins.alterarStatus(True)

print("Instancia da classe Pessoa: ")
print(', '.join("%s: %s" % item for item in attrs.items()))

pessoa_ins.alterarStatus(False)

print("Instancia da classe Pessoa: ")
print(', '.join("%s: %s" % item for item in attrs.items()))