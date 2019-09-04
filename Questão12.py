# Programa de pesquisa de dados

# Coletar dados de idade, sexo e salário dos usuários.

entradas = 0
mulheres = 0
homens = 0
nãoInformados = 0
recebeMais1500 = 0
recebeMenos1500 = 0
Maior = 0
Menor = 1000000000000000000000
idadeMaior = 0
sexoMaior = 0
idadeMenor = 0
sexoMenor = 0
acumulaValor = 0

while True: 

    idade = int(input('Digite a idade (digite uma idade negativa para sair do programa): '))

    if idade < 0:
        break

    sexo = input(('Digite M para Masculino, F para Feminino e NF para não informado: '))
    valor = float(input('Valor do salário: '))

    entradas += 1
    acumulaValor += valor
    
   
    if valor > Maior:
        Maior = valor
        idadeMaior = idade
        sexoMaior = sexo

        if valor < Menor:
            Menor = valor 
            idadeMenor = idade
            sexoMenor = sexo
    else:
        Menor = valor
        idadeMenor = idade
        sexoMenor = sexo
        

    if sexo == 'M':
        homens += 1 

        if valor < 1500:
            recebeMenos1500 += 1
            porcentagem = recebeMenos1500 / entradas

    elif sexo == 'F':
        mulheres += 1

        if valor > 1500:
            recebeMais1500 += 1

    else: 
        nãoInformados += 1



    mediadeSalarios =  float(acumulaValor / entradas) * 100

print(f'A média dos salários é: R$ {mediadeSalarios}')
print(f'A quantidade de mulheres que recebem mais que R$ 1500: {recebeMais1500}')
print(f'A porcentagem de homens que recebem menos que R$ 1500: {porcentagem}%')
print('A idade e o sexo da pessoa que recebe o maior e o menor valor: ')
print(f'Menor: Idade: {idadeMenor}  Sexo: {sexoMenor}')
print(f'Maior: Idade: {idadeMaior}  Sexo: {sexoMaior}')
