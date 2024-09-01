from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# instancia da classe Pessoa
pessoa = Pessoa("Joao", "378446", "01/08/2024", "Ativa")
pessoa.imprimir_informacoes()

print("\n")

#instancia da classe PessoaFisica
pessoafisica = PessoaFisica("Mariana", "456789", "01/01/2015", "Ativa", "01/01/1980", "89.456.123-12", "983004058")
pessoafisica.imprimir_informacoes()

print("\n")

#instancia da classe PessoaJuridica
pessoajuridica = PessoaJuridica("Empresa Python", "1234567", "01/01/2024", "Ativa", "01/12/2023","07.882.442/")
pessoajuridica.imprimir_informacoes()

# Alteracao de Valores via Setter

pessoa.nome = "Joao Chaves"
pessoafisica.cpf = "444.555.666-77"
pessoajuridica.cnpj = "08.888.888/0001-85"

print("\nApos alteracoes")
pessoa.imprimir_informacoes()
pessoafisica.imprimir_informacoes()