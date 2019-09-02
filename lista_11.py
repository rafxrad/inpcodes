
usuarios = 0
Entre12e21 = 0
Altura12e21 = 0
Mais70 = 0
Mais90 = 0
AcumulaPeso = 0
AcumulaIdade = 0
AcumulaAltura = 0

for usuario in range(1, 11):

    idade = int(input("Por favor, digite a idade: "))
    altura = float(input("Por favor, digite a altura em m: "))
    peso = float(input("Por favor, digite o peso: "))

    usuarios = usuarios + 1
    AcumulaPeso = AcumulaPeso + peso
    AcumulaIdade = AcumulaIdade + idade
    AcumulaAltura = AcumulaAltura + altura

    if idade >=12 and idade <= 21:
        Entre12e21 = Entre12e21 + 1
        Altura12e21 = Altura12e21 + altura

    elif peso > 70 and peso <= 90:
        Mais70 = Mais70 + 1
        

    elif peso > 90 and altura < 1.90:
        Mais90 = Mais90 + 1



# Médias

mediaPeso = AcumulaPeso / usuarios
mediaIdade = AcumulaIdade / usuarios
mediaAltura = AcumulaAltura / usuarios
mediaAltura12 = Altura12e21 / Entre12e21

print("Número de entradas: ", usuarios)
print('Média da altura dos usuários: ', mediaAltura)
print('Média do peso dos usuários: ', mediaPeso)
print('Média da idade dos usuários: ', mediaIdade)
print('Pessoas +70 kg: ', Mais70)
print('Pessoas +90 kg: ', Mais90)
print('Pessoas entre 12 e 21 anos: ', Entre12e21)
print('Média de altura das pessoas entre 12 e 21 anos: ', mediaAltura12)
