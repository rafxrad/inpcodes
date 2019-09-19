
# programa para incluir pedidos de pizza.


pedido = {'ingrediente': '', 'borda': '', 'bebida': ''}

print('Bem-vindo a Pizzaria Top Chef! Vamos realizar seu pedido?')
while True:

    ingrediente = input('digite o ingrediente (digite quit para sair): ')

    if ingrediente == 'quit':
        break
    else:
        pedido['ingrediente'] += ingrediente + '\n'
        print('Você incluiu ', ingrediente)
        continuar = input('deseja adicionar mais ingredientes? S/N: ')
        if continuar == 'S'.lower():
            continue
        else:
            borda = input('digite como quer a borda: ')
            bebida = input('bebida desejada: ')
            pedido['borda'] += borda + '\n'
            pedido['bebida'] += bebida + '\n'

            finalizar = input('Deseja finalizar o pedido? S/N: ')

            if finalizar == 'S'.lower():
                break
            else:
                continue
        
       
print('--------------------------------------------')
print('Sua pizza possui os seguintes ingredientes:')
for key, value in pedido.items():
    print(key,':\n', value)

print('Obrigado! Volte sempre.')
