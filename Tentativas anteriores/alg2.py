import copy
class Fornecedor:
  def __init__(self,ide,itens):
      self.ide=ide
      self.itens = itens


class Celula:
  def __init__(self,contador,lista):
      self.contador=contador
      self.listaFoncedor = lista
  def __repr__(self):
      return ''+str(self.contador)+'-'+str(self.listaFoncedor)

listaCompras=[1,2,4,6,8]
fornecedores=[]
fornecedores.append(Fornecedor('F4',[1,2,4,6,8]))
fornecedores.append(Fornecedor('F3',[1,2,5,6,8]))
fornecedores.append(Fornecedor('F1',[1,2,3,6,7]))
fornecedores.append(Fornecedor('F2',[1,2,4,5,7]))


def solucao_fornecimento(listaItem,idItem,fornecedores,idFornecedor,temp, memoria,ultimo,ultimoArgumento):
    if(idItem==len(listaItem)):
        return Celula(0,[])
    if(ultimo==idFornecedor and ultimoArgumento==False):
        return Celula(float('inf'),[])
    if(ultimo==idFornecedor and ultimoArgumento==True):
        ultimoArgumento=False
    #if(memoria[idItem][idFornecedor]==None):    
    if(listaItem[idItem] in fornecedores[idFornecedor].itens):
            # quebrei min (primeiraChamada, segundaChamada)
          primeiraChamada=solucao_fornecimento(listaItem,idItem+1,fornecedores,idFornecedor,temp,memoria,idFornecedor,True)
          segundaChamada=solucao_fornecimento(listaItem,idItem,fornecedores,((idFornecedor+1)%len(fornecedores)),temp,memoria,ultimo,ultimoArgumento)
          print("Item:",idItem,"fornecedor:",idFornecedor)    
          print("Primeiro",primeiraChamada)
          print("Segundo",segundaChamada, ((idFornecedor+1)%len(fornecedores)))
          if(primeiraChamada.contador<=segundaChamada.contador):
              if (fornecedores[idFornecedor].ide not in primeiraChamada.listaFoncedor):
                  primeiraChamada.listaFoncedor.append(fornecedores[idFornecedor].ide)
              memoria[idItem][idFornecedor]=Celula(len(primeiraChamada.listaFoncedor),primeiraChamada.listaFoncedor.copy)
          elif(primeiraChamada.contador>segundaChamada.contador):
              if (fornecedores[idFornecedor].ide not in segundaChamada.listaFoncedor):
                  segundaChamada.listaFoncedor.append(fornecedores[idFornecedor].ide)
              memoria[idItem][idFornecedor]=Celula(len(segundaChamada.listaFoncedor),segundaChamada.listaFoncedor.copy)
            
##              if("ERRO"==primeiraChamada and "ERRO"!=segundaChamada):
##                  print("To aqui 1")
##                  #if (fornecedores[idFornecedor].ide not in segundaChamada):
##                      #segundaChamada.append(fornecedores[idFornecedor].ide)
##                  memoria[idItem][idFornecedor]=segundaChamada.copy()
##              elif("ERRO"==segundaChamada and "ERRO"!=primeiraChamada):
##                  print("To aqui 2")
##                  if (fornecedores[idFornecedor].ide not in  primeiraChamada):
##                      primeiraChamada.append(fornecedores[idFornecedor].ide)
##                  memoria[idItem][idFornecedor]=primeiraChamada.copy()
##              elif("ERRO"==segundaChamada and "ERRO"==primeiraChamada):
##                  print("To aqui 3")
##                  memoria[idItem][idFornecedor]=segundaChamada
##              elif(len(primeiraChamada)<=len(segundaChamada)):
##                  print("To aqui 4")
##                  if (fornecedores[idFornecedor].ide not in primeiraChamada):
##                      primeiraChamada.append(fornecedores[idFornecedor].ide)
##                  memoria[idItem][idFornecedor]=primeiraChamada.copy()
##              elif(len(primeiraChamada)>=len(segundaChamada)):
##                  print("To aqui 5")
##                  #if (fornecedores[idFornecedor].ide not in segundaChamada):
##                  #    segundaChamada.append(fornecedores[idFornecedor].ide)
##                  memoria[idItem][idFornecedor]=segundaChamada.copy()
##              else:
##                  print("To aqui 6")
##                  memoria[idItem][idFornecedor]=segundaChamada.copy()

          #else:
          #    temp2=temp.copy()
          #    temp2.append(fornecedores[idFornecedor].ide)
          #    memoria[idItem][idFornecedor]=min(solucao_fornecimento(listaItem,idItem+1,fornecedores,idFornecedor,temp2,memoria,idFornecedor,True),solucao_fornecimento(listaItem,idItem,fornecedores,((idFornecedor+1)%len(fornecedores)),temp.copy(),memoria,ultimo,ultimoArgumento))     
    else:
        memoria[idItem][idFornecedor]=solucao_fornecimento(listaItem,idItem,fornecedores,((idFornecedor+1)%len(fornecedores)),temp,memoria,ultimo,ultimoArgumento)
    #print(temp,idItem,idFornecedor)
##    else:
##      print("memoria")
##    print("matriz")
##    for value in memoria:
##        print(value)
##    if type(memoria[idItem][idFornecedor].listaFoncedor) is list:
##      return copy.copy(memoria[idItem][idFornecedor])
##    else:
##      return memoria[idItem][idFornecedor]

     

a=solucao_fornecimento(listaCompras,0,fornecedores,0,Celula(0,[]),[[Celula(0,[]) for _ in range(len(fornecedores))] for _ in range(len(listaCompras))],0,True)

print("Solucao:", a)
