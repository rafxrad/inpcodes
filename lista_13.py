# Programa oferece opções para calcular médias.

print('Bem-vindo ao Calculador de Médias! Nesse programa você pode calcular a média de 2 formas diferentes.')
print('\t\t\t\tMENU DE OPÇÕES\nPor favor, digite o número da opção desejada.')
print('1. Média Aritmética\n2. Média Ponderada\n3. Sair')

# Entrada do usuário
opc = int(input())

# Define variáveis para o laço.

nota1 = 0
nota2 = 0
nota3 = 0
peso1 = 0
peso2 = 0
peso3 = 0

# Se a opção for diferente de 3 (sair), executa as condições.

while opc != 3: 
    
    # Usuário digitou 1 para média aritmética
    if opc == 1: 
      print('Digite duas notas que vão ser calculadas. Insira um valor negativo para sair')
      nota1 = float(input('Digite a nota 1: '))
      # Usuário tem a opção de sair digitando a nota negativa para a primeira nota.
      # Caso não digite, o laço continua a ser executado.

      # Digitou a nota positiva.
      if nota1 > 0:
        nota2 = float(input('Digite a nota 2: '))
        mediaAritmetica = (nota1 + nota2) / 2
        print('A média aritmética é: ', mediaAritmetica)

      # Usuário digitou nota negativa, então o laço para de executar.
      else:
        print('Até mais!')
        break
        
    # Usuário digitou 2 para média ponderada. Nessa opção são solicitadas notas e pesos. 
    elif opc == 2:

      # Usuário tem a opção de sair digitando a nota negativa na primeira vez. 
      # Caso não digite, o laço continua a ser executado.
      print('Digite as notas e os pesos a serem calculados. Insira um valor negativo para sair')
      nota1 = float(input('Digite a nota 1: '))

    # Usuário digitou a nota positiva. 

      if nota1 > 0: 
        peso1 = float(input('Digite o peso da nota 1: '))
        nota2 = float(input('Digite a nota 2: '))
        peso2 = float(input('Digite o peso da nota 2: '))
        nota3 = float(input('Digite a nota 3: '))
        peso3 = float(input('Digite o peso da nota 3: '))
        mediaPonderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3*peso3)) / (peso1 + peso2 + peso3)
        print('A média ponderada é: ', mediaPonderada)
      
      #  Usuário digitou nota negativa. O programa para de executar.
      else:
        print('Até mais!')
        break

# Digitou 3 para sair.
else:
  print('Até mais!')
