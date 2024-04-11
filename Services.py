produtos = ({})  # Lista vazia para armazenar os produtos

def adicionar_produto(lista, total_produtos): 
    # Adiciona um novo produto à lista de produtos.
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))
    valor_unitario = float(input('Digite o valor unitário do produto: '))

    total_produto = quantidade * valor_unitario
    total_produtos += total_produto

    produto = {'produto': nome, 'quantidade': quantidade, 'valor': valor_unitario, 'total': total_produto}
    lista.append(produto)

    print('Produto adicionado com sucesso!')
    return total_produtos

def ver_lista(lista, total_produtos):
    #Exibe a lista de produtos e o total acumulado de preços de todos os produtos
    print('''\n=== Lista de Produtos ===''')
    for produto in lista:
        print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']}, Total: R${produto['total']}")
    print(f"Valor Total de Todos os Produtos: R${total_produtos}")
def ver_lista_produtos_por_categoria(categoria):
      # Exibe os produtos filtrados por categoria
    for produto in produtos:
        if produto['categoria'] == categoria:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Categoria: {produto['categoria']}")
    if not any(produto['categoria'] == categoria for produto in produtos):
        print("Nenhum produto encontrado para esta categoria.")
def atualizar_produto(lista, total_produtos):
    # Atualiza as informações de um produto existente na lista de produtos.
    nome = input('Digite o nome do produto que deseja atualizar: ')
    for produto in lista:
        if produto['produto'] == nome:
            print('Produto encontrado:')
            print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: R${produto['valor']}, Total: R${produto['total']}")
            quantidade = int(input('Digite a nova quantidade: '))
            valor_unitario = float(input('Digite o novo valor unitário: '))
            produto['quantidade'] = quantidade
            produto['valor'] = valor_unitario
            produto['total'] = quantidade * valor_unitario
            total_produtos = sum(p['total'] for p in lista)
            print('Produto atualizado com sucesso!')
            return total_produtos
    print('Produto não encontrado.')

def remover_produto(lista, total_produtos):
     #Remove um produto da lista de produtos
    nome = input('Digite o nome do produto que deseja remover: ')
    for produto in lista:
        if produto['produto'] == nome:
            total_produtos -= produto['total']
            lista.remove(produto)
            print('Produto removido com sucesso!')
            return total_produtos
    print('Produto não encontrado.')
