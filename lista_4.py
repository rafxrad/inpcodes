# Programa que calcula raio, perímetro e área de circunferência a partir do diâmetro.

diametro = float(input('Por favor, digite o diâmetro em cm: '))

pi = 3.14
raio = diametro / 2
P = 2 * pi * raio
A = pi * (raio ** 2)

print('Raio: ', raio, "cm")
print('Perímetro: ', P, 'cm')
print('Área: ', A, 'cm')