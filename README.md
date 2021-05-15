# minimo_fornecedores

# Descrição da atividade
Problema I – Sistema de Vendas Seja I um conjunto de itens, F um conjunto de fornecedores e
T uma tabela de preços, onde cada linha da tabela é um elemento de uma tupla F × I × R que
identifica um fornecedor, um item e o seu respectivo preço por unidade ou por kg. Como estamos
em tempo de pandemia, todas as entregas são feitas na casa do cliente e cada fornecedor cobra
um valor de frete para a entrega. Os preços dos fretes estão em uma tabela V cujos elementos
são pares F × R. Após os recebimento das compras, os clientes podem avaliar os fornecedores
e essa informação fica armazenada em uma tabela A ⊆ F × {1, 2, 3, 4, 5}. Usando esse dados,
construa um sistema de vendas em que o cliente escolha os produtos que deseja e suas respectivas
quantidades (que podem ser um número inteiro ou um número real, dependendo da unidade de
venda), e sistema devolva a melhor compra possível, considerando:
- o menor número total de fornecedores para a compra

# Código que retorna o menor número total de fornecedores
minimoFornecedores.py

# Entradas esperadas
- Para a lista de compras o arquivo é denominado: lista_compras.csv
    - A estrutura do lista_compras é dado por: id do item, quantidade 
- Para a lista de itens com os fornecedores, seus itens, valores é o arquivo: entrada.csv
    - A estrutura da entrada é dada por: fornecedor, id do item, valor, unidade do item se é kg ou unidade
- Para os valores de frete de cada fornecedor é utilizado o arquivo: frete.csv 
    - Que contém em cada linha: fornecedor, valor do frete