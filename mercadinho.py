# Programa para gerenciar o estoque de um mercadinho e receber pedidos.

# Atribuindo dois vetores com 10 posições, um para os códigos de produto e outro para quantidade disponível.

codigoProdutos = list(range(10))
quantidadeProdutos = [10, 10, 10, 10 , 10, 10, 10, 10, 10]
codigoCliente = 1

# Mensagem de boas vindas! 

print('Bem vindo ao Mercadinho Tabajara! Faça sua compra online!')
print('----------------------------------------------------------')
print('Precisamos do seu código Fidelidade Tabajara!')
while True:
    codigoCliente = int(input('Digite o código do cliente (digite 0 para sair): '))
    # Se o código do cliente for zero, pare o programa.
    if codigoCliente == 0:
        break
    # Caso não seja, o programa pedirá uma nova informação.
    else:
        # Informando o código do produto
        print('Produtos disponíveis:')
        print('0 - Água Mineral 500ml\n1 - Abacaxi (un)\n2 - Sabão em pó (kg)'
        '\n3 - Creme Dental Colgate\n4 - Margarina Qualy (250g)\n5 - CD Reginaldo Rossi Ao Vivo (un)\n6 - Bala Dentadura Iogurte (un)'
        '\n7 - Chinela Havaiana Branca da Tira Azul (un)\n8 - Camisinha (pct)\n9 - Chocolate Garoto (cx))')
        codigoDigitado = int(input('Digite o código do produto desejado (0-9): '))
        
        if codigoDigitado in codigoProdutos:
            # Se o código digitado está inserido na lista de códigos de produto, pede-se a quantidade.

            quantidade = int(input('Quantidade do produto: '))
            
            # Igualando a quantidade ao valor no índice desejado, se essa quantidade for > 0,
            # o programa desconta do valor atual.
            # Pedido realizado com sucesso.

            if quantidadeProdutos[codigoDigitado] > 0:
                quantidadeProdutos[codigoDigitado] -= quantidade
                print('Pedido recebido, obrigado. Volte sempre!')
                # Volta ao código do cliente, onde o usuário pode optar por inserir novo pedido ou sair.
                continue

            # Caso a quantidade seja zero ou inferior, o programa mostra que o estoque é insuficiente.
            # Não é possível realizar o pedido.

            else:
                print('Estoque insuficiente. Tente novamente')
                break

        # Se o código do produto não existe, mostra-se um erro ao usuário.

        else:
            print('ERRO 404. CÓDIGO DE PRODUTO INEXISTENTE')
            break

# Ao sair do programa, exibirá o estoque atualizado com os produtos e quantidades disponíveis.

print('----------------------------------------------')
print('Estoque atualizado: ')
print('Código dos produtos disponíveis: ', codigoProdutos)
print('Quantidade disponível: ', quantidadeProdutos)