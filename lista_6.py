# Programa recebe dois números e executa as opções:
# 1. Média dos números digitados
# 2. Diferença do maior pelo menor
# 3. Produto dos números digitados
# 4. Divisão do primeiro pelo segundo (a segunda entrada não pode ser zero)

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('\n\nSelecione uma das opções abaixo: \n1 - Média dos números\n2 - Diferença do maior pelo menor\n3 - Produto dos números\n4 - Divisão do primeiro pelo segundo\t')

userChoice = int(input())


if userChoice == 1:
    media = (num1 + num2) / 2
    print('A média dos números é, ', media)

elif userChoice == 2:
    if num1 > num2:
        sub = num1 - num2
        print('\nA subtração do maior número pelo menor é: ', sub)
    else:
        sub = num2 - num1
        print('\nA subtração do maior pelo menor é: ', sub)

elif userChoice == 3:
    prod = num1 * num2
    print('\nO produto dos números é: ', prod)

elif userChoice == 4:
    if num2 != 0:
        div = num1 / num2
    else:
        print('\nO segundo número deve ser maior que zero para ser possível subtrair!'
        '\nTente novamente!')
else: 
    print('Opção inválida!')
    exit()
