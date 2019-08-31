# Programa para atualização de salário de funcionários.
# O programa recebe o valor de entrada do salário atual e devolve com o aumento dentro da margem.

print('Bem-vindo(a)!')
salarioAtual = float(input('Por favor, digite o valor do salário atual: '))

# Margens de aumento: 50% a 5%.
aumento50 = salarioAtual * 0.50
aumento40 = salarioAtual * 0.40
aumento30 = salarioAtual * 0.30
aumento20 = salarioAtual * 0.20
aumento10 = salarioAtual * 0.10
aumento5 = salarioAtual * 0.05

if salarioAtual <= 300:
    salarioNovo = salarioAtual + aumento50

elif salarioAtual > 300 and salarioAtual <= 500:
    salarioNovo = salarioAtual + aumento40

elif salarioAtual > 500 and salarioAtual <= 700:
    salarioNovo = salarioAtual + aumento30

elif salarioAtual > 700 and salarioAtual <= 800:
    salarioNovo = salarioAtual + aumento20

elif salarioAtual > 800 and salarioAtual <= 1000:
    salarioNovo = salarioAtual + aumento10

else:
    salarioNovo = salarioAtual + aumento5
    
valorFinal = 'O valor do salário atualizado é: R$' + str(salarioNovo)
print(valorFinal)