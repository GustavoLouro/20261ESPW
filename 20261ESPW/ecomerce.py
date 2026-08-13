#Exercício 1 - Cadastro de produtos

def cadastrar_produto(catalogo, nome, preco, estoque):
  produto = [nome, preco, estoque]
  catalogo.append(produto)
  return catalogo

def exibir_catalogo(catalogo):
  for produto in catalogo:
    print(f'{produto[0]} - R${produto[1]:.2f} , (estoque:{produto[2]})')


#Nesse caso, o catálogo é uma lista de listas, onde cada produto é representado por uma lista contendo o nome, preço e estoque. A função cadastrar_produto adiciona um novo produto ao catálogo, enquanto a função exibir_catalogo percorre a lista de produtos e imprime suas informações formatadas.

# print(f'Produto cadastrado: {novos_produtos[0]}')

if __name__ == "__main__":
  novos_produtos = []
  novos_produtos = cadastrar_produto(novos_produtos, nome="Camiseta azul", preco=59.90, estoque=120)
  novos_produtos = cadastrar_produto(novos_produtos, nome="Tenis Runner", preco=129.90, estoque=50)
  novos_produtos = cadastrar_produto(novos_produtos, nome="Bone Preto", preco=39.90, estoque=20)

exibir_catalogo(novos_produtos)

