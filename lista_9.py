# O programa recebe a entrada de tipos de investimento e devolve o valor corrigido
# após um mês de investimento.

print('Escolha o tipo de investimento: '
'\n1 - Poupança'
'\n2 - Fundos de Renda Fixa')

tipo = int(input())

print('Insira o valor investido: ')
valor = float(input())

poupança = valor * 0.03
rendaFixa = valor * 0.04

if tipo == 1:
    totalCorrigido = valor + poupança

else:
    totalCorrigido = valor + rendaFixa

print('Valor corrigido: R$', totalCorrigido)
