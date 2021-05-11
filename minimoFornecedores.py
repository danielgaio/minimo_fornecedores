import copy, csv

class Fornecedor:
    def __init__(self, ide, itens,frete):
        self.ide = ide
        self.itens = itens
        self.cont = 0
        self.frete = frete
        self.itemPegos=set()
        self.valor = 0.0

    def __repr__(self):
        return  str(self.ide)

class Item:
    def __init__(self, ide, valor, unidade):
        self.ide = ide
        #self.nome = nome
        self.valor = valor
        self.unidade = unidade
        #self.fornecedor  = fornecedor

    def calcPreco(self,quantidade):
        return float(self.valor) * float(quantidade)
    
    def __repr__(self):
        return  str(self.ide)

class ItemCompra:
    def __init__(self, ide, quantidade):
        self.ide = ide
        self.quantidade = quantidade
    def __repr__(self):
        return  str(self.ide) + " Qnt:"+str(self.quantidade)


# listaCompras = []
# listaCompras.append(ItemCompra(1,5))
# listaCompras.append(ItemCompra(2,0.3))
# listaCompras.append(ItemCompra(5,1))
# listaCompras.append(ItemCompra(7,2))

#==========================================================
#Leitura do arquivo da lista de compras onde cada linha possui: id do item, quantidade
# print("Lista Compras")
listaCompras=[]
with open('lista_compras.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        # print("Item: ", row[0])
        # print("Quantidade: ", row[1])
        listaCompras.append(ItemCompra(row[0],row[1]))

# print("----------------")

fornecedores = {}

#==========================================================
# Leitura do arquivo da lista de fornecedores, criação de dicionario, filtrando e agrupando por fornecedor
with open('entrada.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        if(int(row[0]) in fornecedores):  # esse aqui caminha fornecedores coluna 
            fornecedores[int(row[0])].itens[row[1]]=Item(row[1],row[2],row[3]) # add item coluna
            fornecedores[int(row[0])].frete=row[4]
        else:
            fornecedores[int(row[0])] = Fornecedor(row[0], {row[1]:Item(row[1],row[2],row[3],)},row[4])
           # fornecedores[int(row[0])].append(int(row[1])) # adiciona item  no fornecedor


matriz=[]


# # #https://github.com/Nathalino/multiplicacaoMatriz/blob/master/matriz.php
# # inicia a matriz de 3 dimensões. Cada célula da matriz armazena um conjunto de fornecedores
# # são 3 dimensões porque é necessária uma matriz bidimensional para cada fornecedor, 
# # que contém a relação item x item (ver multiplicação de matrizes)
# # dessa forma se tem uma 'lista de matrizes 2D'
# # o algortimo funciona preenchendo cada uma dessas matrizes considerando de cada vez
# # um fornecedor diferente como ínicio da procura por itens

# # =======================
# # Preenchimento da matriz com sets vazios
c = 0
while c < len(fornecedores):
    matriz.append([])
    a=0
    while a < len(listaCompras)+1:
        b = 0
        matriz[c].append([])
        while b < len(listaCompras)+1:
            matriz[c][a].append(set())
            b += 1
        a += 1
    c += 1

# # =================================
# # Preencher a diagonal principal -> CASO BASE
cont = 0 # cont percorre a parte [][i][j] da matriz 3D, i e j são item x item
while cont < len(fornecedores): # percorre todas matrizes de fornecedores
    # inicio de qual fornecedor deve iniciar loop
    copiaFornecedores=copy.copy(fornecedores)
    for key, value in enumerate(listaCompras): # percorre os itens da lista de compras
        inicio = cont
        verificado = True
        
        while (inicio % len(copiaFornecedores) != cont or verificado):
            # a lista de fornecedores é lida a cada iteração começando de uma posição diferente,
            # por exemplo, no loop 1 ela vai ler forn 1 como o primeiro, loop 2 forn 2, de forma circular
            # como ele pega o primeiro fornecedor que tem o item, começando de pontos diferentes gera resultados diferentes.
            calculaProximoFonecedor = (inicio % len(copiaFornecedores)) # com o resto se consegue pegar qual é o próximo - lista circular
            #print(list(copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]].itens.keys()))
            #print(value.ide)
            if(str(value.ide) in list(copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]].itens.keys())): # aqui verifica se o forn tem o item,
                copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]].itemPegos.add(value)
                #print (copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]].itens[str(value.ide)].calcPreco(value.quantidade))
                copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]].valor+=(copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]].itens[str(value.ide)].calcPreco(value.quantidade))
                matriz[cont][key+1][key+1].add(copiaFornecedores[list(copiaFornecedores.keys())[calculaProximoFonecedor]]) #  add ele na diagonal desse item
                break    
            else:
                inicio += 1
                verificado = False
    cont += 1





# # =====================
# #  Preenchimento das diagonais superiores das matrizes - resposta no canto superior direito - ignorar 
tamanho = len(listaCompras)
respostaFinal = set()
f = 0
while f < len(fornecedores): # matriz externa, uma matriz 2d para cada fornecedor
    for L in range(2, tamanho + 1): # é uma maneira de preencher apenas a diagonal superior
        for i in range(1, tamanho - L + 2):
            j = i + L - 1
            for k in range(i,j):
                matriz[f][i][j].update(matriz[f][k+1][j])
                matriz[f][i][j].update(matriz[f][i][k])

    # resultado final entre todas as matrizes: vefifica a que tem menos fornecedores, depois caso haja empate, pega pelo menor frete
    if len(respostaFinal) == 0: # se vazio add atual
        respostaFinal = matriz[f][1][tamanho] # a resposta de cada matriz sempre estará na célula do canto sup direito
    elif len(respostaFinal) > len(matriz[f][1][tamanho]): # se o atual é menor que o salvo, guarda atual
        respostaFinal = matriz[f][1][tamanho]
    elif len(respostaFinal) == len(matriz[f][1][tamanho]): # se é igual tam, compara fretes
        freteAtual = 0
        itemAtual=0
        freteResposta = 0
        itemsResposta=0
        for forn in matriz[f][1][tamanho]: # soma fretes dos fornecedores do resultado atual
            freteAtual += forn.frete
            itemAtual+=forn.valor
        for forn in respostaFinal: # soma fretes do resultado anterior
            freteResposta += forn.frete
            itemsResposta+=forn.valor
        if freteAtual < freteResposta: # pega o resultado atual se frete total for menor
            respostaFinal = matriz[f][1][tamanho]
    f += 1        

# #aqui so para printar as matrizes     
quantidade = len(fornecedores)
linhas = len(matriz[0])
colunas = len(matriz[0])

print("O número mínimo de fornecedores é: ", len(respostaFinal), "|| Sendo que os fornecedores são os seguintes: ", respostaFinal)
# print("Resposta Final:", respostaFinal)
print("\n")

print("Os itens e quantidades de cada fornecedor são:")
for resp in respostaFinal:
    print("Fornecedor:", resp, " = ",resp.itemPegos)
print("\n")
valorFrete=0
valorItem=0

for forn in respostaFinal: # soma fretes do resultado anterior
    valorFrete+=float(forn.frete)
    valorItem+=forn.valor

print("O frete da compra é R$", str(valorFrete), "|| Preço total da compra sem o frete é R$", str(valorItem), "|| Preço total da compra com o frete é R$", str(valorFrete+valorItem))
print("\n")
impressaoMatriz = "-1"

while (impressaoMatriz != "1" and impressaoMatriz != "2"):
    impressaoMatriz = input("Você deseja verificar as matrizes criadas e preenchidas? \n 1) Sim 2) Não \n Digite sua resposta:")

if(impressaoMatriz == "1"):
    for f in range(quantidade):
        print("Matriz: %s"%f)
        for i in range(linhas):
            for j in range(colunas):
                if(j == colunas - 1):
                    print("%s" %matriz[f][i][j])
                else:
                    print("%s" %matriz[f][i][j], end = "  ")

