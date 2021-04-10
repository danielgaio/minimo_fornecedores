import csv

# Pré Processamento

#Leitura do CSV capturando apenas o fornecedor e item em uma nova matriz chamada dados

#Ordenar a matriz agrupando itens por fornecedor, ou seja, f1 - todos os seus itens, f2 - todos os seus itens,...

# Pegar lista de compras e verificar em cada fornecedor quantos itens da lista ele possui e armazenar em um vetor quantidade_itens_fornecedor sendo: [2, 4, 1, 0] => [f1, f2, f3, f4]




# listaCompras=[1,2,4,6,8] 
fornecedores={}
# fornecedores.append(Fornecedor('F1',[1,2,3,6,7,9]))
# fornecedores.append(Fornecedor('F2',[1,2,4,5,7]))
# fornecedores.append(Fornecedor('F3',[1,2,5,6,8]))
# fornecedores.append(Fornecedor('F4',[1,2,32,6,8]))
# # quantidade total produtos variados.
# quantidadeItemTotal=10

# Leitura do arquivo da lista de fornecedores, criação de dicionario, filtrando e agrupando por fornecedor
with open('entrada.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if(int(row[0]) in fornecedores):  # verifica se fornecedor existe no dicionario
            if(int(row[1]) not in fornecedores[int(row[0])]): # verifica se itens existe no fornecedor
                fornecedores[int(row[0])].append(int(row[1]))
        else:
            fornecedores[int(row[0])]=[]#cria fornecedor no dificionario
            fornecedores[int(row[0])].append(int(row[1])) #adiciona item  no fornecedor
print(fornecedores)   
# Leitura de arquivo da lista de compras
#verificar qual fornecedor tem quais itens da lista

quantidade_itens_fornecedor = []

for a in fornecedores:
    quantidade_itens_fornecedor.append(0)
listaCompras=[]
with open('lista_compras.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        listaCompras.append(int(row[0]))
        for chave in fornecedores:
            if(int(row[0]) in fornecedores[chave]):
                    quantidade_itens_fornecedor[chave-1]+= 1

print("Lista: ", listaCompras)
#print(fornecedores)
print("Qtd itens cada forn.:", quantidade_itens_fornecedor)
qtd_itens_lista = len(listaCompras)
print(qtd_itens_lista)


# Função Recursiva

#qtd_itens_lista = 10    # quantidade de itens sendo comprados, 10 eh exemplo
#listaComplas=[]
# moedas[] equivale ao vetor quantidade_itens_fornecedor

# quantidade_itens_fornecedor = [2, 4, 1, 6]

quantidade_fornecedores = len(quantidade_itens_fornecedor)

memoria = [[None for _ in range(qtd_itens_lista + 1)] for _ in range(quantidade_fornecedores)] #insere none 

# print(memoria)
#inf = 9999999999999
def solucao_fornecimento(listaItem,idItem,fornecedores,idFornecedor,temp):
    if(idItem==len(listaItem) or len(fornecedores)==idFornecedor): # todos os itens foram comprados ou fornecidos
        return 0
    if(memoria[indice_fornecedor_atual][quantidade_restante] == None):
        if(listaItem[idItem] in fornecedores[idFornecedor]):
            if()
            
            pega_produto=solucao_fornecimento(listaItem,idItem,fornecedores,idFornecedor+1,temp)    
            pega_produto = 
        nao_pega_produto = solucao_fornecimento(quantidade_restante,indice_fornecedor_atual+1)
        memoria[indice_fornecedor_atual][quantidade_restante]=min(pega_produto,nao_pega_produto)
        #print(pega_produto)
        #print(nao_pega_produto)
    return memoria[indice_fornecedor_atual][quantidade_restante]

print(solucao_fornecimento(int(qtd_itens_lista)))
