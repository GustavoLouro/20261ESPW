🛒 Cadastro de Produtos — E-commerce Simples
Este projeto é um script em Python desenvolvido para exemplificar a gestão básica de um catálogo de produtos para e-commerce. Ele demonstra o uso de estruturas de dados fundamentais (listas de listas) e funções para cadastrar e listar itens com preço e quantidade em estoque.

🚀 Funcionalidades
cadastrar_produto: Adiciona um novo item (nome, preço e estoque) ao catálogo.

exibir_catalogo: Percorre a lista de produtos e imprime as informações formatadas na tela.

🛠️ Tecnologias Utilizadas
Python 3.x

📂 Como Executar o Projeto
Clone o repositório:

Bash
git clone https://github.com/GustavoLouro/20261ESPW.git
Navegue até a pasta do projeto:

Bash
cd 20261ESPW/20261ESPW
Execute o script Python:

Bash
python ecomerce.py
💻 Exemplo de Saída
Ao rodar o arquivo ecomerce.py, a saída gerada no console será:

Plaintext
Camiseta azul - R$59.90 , (estoque:120)
Tenis Runner - R$129.90 , (estoque:50)
Bone Preto - R$39.90 , (estoque:20)
📝 Estrutura de Dados
O catálogo é estruturado como uma lista de listas:

Python
# [Nome, Preço, Estoque]
catalogo = [
    ["Camiseta azul", 59.90, 120],
    ["Tenis Runner", 129.90, 50],
    ["Bone Preto", 39.90, 20]
]
