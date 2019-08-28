# Programa que calcula a comissão sobre vendas realizadas.

salario = float(input('Digite o valor do salário do funcionário: '))
vendas = float(input('Digite o valor das vendas: '))

# O funcionário recebe um salário fixo e uma comissão de 4% em cima do valor das vendas.

comissao = vendas * 0.04

salarioAbono = salario + comissao

print('Comissão: R$ ', comissao)
print('Salário + Comissão: R$', salarioAbono)


