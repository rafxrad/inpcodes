# Função recebe uma matriz e retorna uma lista com o maior elemento de cada linha.

def elementoMaior(matriz):
    maioresElementos = [] # define lista de retorno

    for i in range(len(matriz)): # itera nas linhas da matriz
        for j in range(len(matriz[0])): # itera nas colunas
            if matriz[i][j-1] > matriz[i][j]: # passa pelo segundo elemento comparando com o anterior
                maioresElementos.append(matriz[i][j-1]) # se é maior que o próximo, retorna ele na lista
    return maioresElementos       # retorna lista dos maiores por linha         

            
        
matrizA = [[2,0],
           [3,1],
          [4,6]]

print(elementoMaior(matrizA))