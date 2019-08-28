# Programa que recebe valor em segundos e converte em HH:MM:SS.

segundos = int(input('Digite o valor dos segundos: '))

segundos_rest = int(segundos % 60)
minutos = int(segundos / 60)
minutos_rest = int(minutos % 60)
hora_rest = int(minutos / 60)

hms = print(f'{hora_rest}:{minutos_rest}:{segundos_rest}')


