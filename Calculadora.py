numero1 = 0
numero2 = 0
operacao = ''


numero1 = int(input('Digite o primeiro numero:'))
operacao = input('Digite a operacao:')
numero2 = int(input('Digite o segundo numero:'))
if operacao == '+':
   resultado = numero1+numero2
elif operacao == '-':
   resultado = numero1-numero2
elif operacao == '*':
   resultado = numero1*numero2
elif operacao == '/':
   resultado = numero1/numero2
else:
    resultado = 'Operação invalida.'
print(str(numero1) + '' + str(operacao) + '' + str(numero2) + ' = ' + str(resultado))  