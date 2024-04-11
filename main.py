import time
from Services import *

produtos = []
total_produtos = 0

while True:
    print('\n=== Lista de Compras ===')
    print('1. Adicionar Produto')
    print('''2. Ver Lista de Produtos
    1. Listar todos os produtos
    2. Filtrar produtos por categoria''')
    print('3. Atualizar Produto')
    print('4. Remover Produto')
    print('5. Sair\n')

    opcao = int(input('Escolha a Opção desejada: '))

    if opcao == 1:
        print('### Você escolheu Adicionar Produto ###')
        adicionar_produto(produtos,total_produtos)  #função para adicionar produto
        time.sleep(2)  # Pausa de 2 segundos
    elif opcao == 2:
        submenu_opcao = int(input('Escolha a opção desejada: '))
        if submenu_opcao == 1:
            ver_lista(produtos,total_produtos)  # função para ver lista de produtos
        elif submenu_opcao == 2:
            categoria = input('Digite a categoria desejada: ')
            ver_lista_produtos_por_categoria(categoria)  # função para ver lista de produtos por categoria
        else:
            print('Opção inválida.')
        time.sleep(2)  # Pausa de 2 segundos
    elif opcao == 3:
        print('### Atualizar Produto ###')
        atualizar_produto(produtos,total_produtos)  # função para atualizar produto
        time.sleep(2)  # Pausa de 2 segundos
    elif opcao == 4:
        print('### Remover Produto ###')
        remover_produto(produtos,total_produtos)  # função para remover produto
        time.sleep(2)  # Pausa de 2 segundos
    elif opcao == 5:
        print('Saindo do programa...')
        break  # Sai do loop while e encerra o programa
    else:
        print('Opção inválida. Tente Novamente.')

print('Fim do programa.')
