# função para interseção de duas listas

lista1 = [2, 3, 4, 5, 6, 7, 8]
lista2 = [4, 5, 10, 8, 12]

def intersecao(lista1, lista2):
    lista3 = [] # lista de interseção
    for i in lista1: # itera na lista 1
        if i in lista2: # condicional para checar se o i está na lista2
            lista3.append(i) # adiciona à interseção
    return lista3 # retorna a interseção

print(intersecao(lista1, lista2))


def intersecao2(lista1, lista2):
    lista3 = [] 
    for i in lista1: 
        for j in lista2:
            if i == j: # itera na lista 2, checando se o i é igual ao j
                lista3.append(i) 
    return lista3 

print(intersecao2(lista1, lista2))