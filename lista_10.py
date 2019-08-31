# Programa recebe o código do produto e quantidade comprada.
# Retorna o preço unitário, preço total da nota, valor do desconto,
# e preço final após o desconto.

print('Bem vindo(a)!')

print('Por favor, digite o código do produto: ')
cod = int(input())

if cod >= 1 and cod <= 10:
    preçoUnitário = 10

elif cod >= 11 and cod <= 20:
    preçoUnitário = 15

elif cod >= 21 and cod <= 30:
    preçoUnitário = 20

elif cod >= 31 and cod <= 40:
    preçoUnitário = 30

else:
    print('Opção inválida! Por favor, digite um número entre 1 e 40.')
    exit()


print('Insira a quantidade de produtos: ')
quant = int(input())


if preçoUnitário == 10:
    totalSemDesconto = 10 * quant

elif preçoUnitário == 15:
    totalSemDesconto = 15 * quant

elif preçoUnitário == 20:
    totalSemDesconto = 20 * quant

else:
    totalSemDesconto = 30 * quant


if totalSemDesconto <= 250:
    valorDesconto = totalSemDesconto * 0.05
    total = totalSemDesconto - valorDesconto
   

elif totalSemDesconto > 250 and totalSemDesconto <= 500:
    valorDesconto = totalSemDesconto * 0.10
    total = totalSemDesconto - valorDesconto
    

else:
    valorDesconto = totalSemDesconto * 0.15
    total = totalSemDesconto - valorDesconto

print('Preço unitário do produto: R$', preçoUnitário )
print('Preço total da nota: R$', totalSemDesconto)
print('Valor do desconto: -R$', valorDesconto)
print('Total final: R$', total)