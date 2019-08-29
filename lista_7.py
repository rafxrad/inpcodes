# Programa recebe valor de dois números e oferece opções de escolha.

num1 = float(input('Por favor, digite o primeiro número: '))
num2 = float(input('Por favor, digite o segundo número: '))

print('Escolha uma das opções abaixo:'
'\na) Primeiro número elevado pelo segundo'
'\nb) Raiz quadrada de cada um dos números'
'\nc) Raiz cúbica de cada um dos números')

opc = input()

if opc == 'a':
    print(num1 ** num2)

elif opc == 'b':
    print('Raiz quadrada do primeiro número: ', num1 ** 0.5)
    print('Raiz quadrada do segundo número: ', num2 ** 0.5)

elif opc == 'c':
    print('Raiz cúbica do primeiro número: ', num1 ** 0.3)
    print('Raiz cúbica do segundo número: ', num2 ** 0.3)

else:
    print("Opção inválida")
    exit()