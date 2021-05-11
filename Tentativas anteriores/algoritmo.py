
# Pré Processamento

# Pré Processamento

#Leitura do CSV capturando apenas o fornecedor e item em uma nova matriz chamada dados

#Ordenar a matriz agrupando itens por fornecedor, ou seja, f1 - todos os seus itens, f2 - todos os seus itens,...

# Pegar lista de compras e verificar em cada fornecedor quantos itens da lista ele possui e armazenar em um vetor quantidade_itens_fornecedor sendo: [2, 4, 1, 0] => [f1, f2, f3, f4]

# Função Recursiva
class Fornecedor:
  def __init__(self,ide,itens):
      self.ide=ide
      self.itens = itens
      self.cont=0
  def contador(self):
      self.cont=self.cont+1

listaCompras=[1,2,4,6]
fornecedores=[]
fornecedores.append(Fornecedor('F1',[1,2,3,6,7]))
fornecedores.append(Fornecedor('F2',[1,2,4,5,7]))
fornecedores.append(Fornecedor('F3',[1,2,5,6,8]))

quantidade_fornecedores = len(fornecedores)
quantidade_item=len(listaCompras)

def solucao_fornecimento(indice_listaCompras,indice_fornecedor_atual):
    if(indice_listaCompras==quantidade_item): 
        return [0,0]
    if (indice_listaCompras<=quantidade_item and indice_fornecedor_atual==quantidade_fornecedores):  
        return float("inf")
    if (listaCompras[indice_listaCompras] in fornecedores[indice_fornecedor_atual].itens):
        valor=[fornecedores[indice_fornecedor_atual].ide,1+solucao_fornecimento(indice_listaCompras+1,indice_fornecedor_atual)[1]]
        #pega_produto =[fornecedores[indice_fornecedor_atual].ide ,1 + (solucao_fornecimento(indice_listaCompras+1,indice_fornecedor_atual)[1])]
    else:
        valor=[fornecedores[indice_fornecedor_atual].ide,0+solucao_fornecimento(indice_listaCompras+1,indice_fornecedor_atual)[1]]
    valor2= [fornecedores[indice_fornecedor_atual].ide,0+solucao_fornecimento(indice_listaCompras,indice_fornecedor_atual+1)[1]]
    if(valor[1]<valor2[1]):
        return valor2
    else:
        return valor
      
    ## [fornecedores[indice_fornecedor_atual+1].ide ,solucao_fornecimento(quantidade_restante,indice_fornecedor_atual+1)[1]]
    ###if(pega_produto[1]>nao_pega_produto[1]):  
    ##    return pega_produto#
    ##else:
    ##    return nao_pega_produto


print(solucao_fornecimento(0,0))
#print (np.matrix(memoria))



