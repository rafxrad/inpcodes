# Programa que calcula a média ponderada de duas notas.
# A primeira nota tem peso 3 e a segunda peso 1. 

nota1 = float(input('Por favor, insira a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

peso1 = 3
peso2 = 1
pesoFinal = peso1 + peso2



mediaPonderada = ((nota1 * peso1) + (nota2 * peso2)) / pesoFinal

print('A média das notas é', mediaPonderada)