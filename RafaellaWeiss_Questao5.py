# função para checar se uma palavra é um palindromo

def checkPalidromo(palavra):
    palavra = palavra.lower() # transforma a palavra em minúscula
    lista = [] # uma lista para a palavra normal
    listaInvertida = [] # lista com a palavra invertida
    status =  False # define o status inicial como falso

    for i in palavra: # iterar pela string e colocar em uma lista
        lista.append(i) 

    for i in range(len(palavra), 0, -1): # iterar na string de trás para frente
        listaInvertida.append(palavra[i-1])        # iterar na string na ordem contrária e adiciona à outra lista
        
     


    if lista == listaInvertida: # compara as listas
        status = True # muda o status

    return status # retorna o status


print(checkPalidromo('ararinha'))
print(checkPalidromo('omississimo'))
print(checkPalidromo('arara'))

