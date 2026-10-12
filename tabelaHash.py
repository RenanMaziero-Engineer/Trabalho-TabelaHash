'''
Renan Maziero
RU: 4691724
'''

class estado:
    
    def __init__(self, sigla=None, nomeEstado=None):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class listaEncadeadaSimples:    
        
    def inserir(self, lista, obj, posicao):
        lista_ = lista
        pos = posicao
        
        if lista_[pos] == None:
            lista_[pos] = obj
            return
        else:
            posicao_atual = lista_[pos]  
            lista_[pos] = obj 
            obj.proximo = posicao_atual          
        
class tabelaHash:
    def __init__(self):
        self.lista_ = [None] * 10 
        self.ls_ = listaEncadeadaSimples()

    def funcHash(self, sigla, nomeEstado):
        
        obj = estado(sigla=sigla, nomeEstado=nomeEstado)
        
        if obj.sigla == 'DF':
            if self.lista_[7] != None:
                print('\nDF já foi inserido\n')
            self.lista_[7] = obj
        
        else:
            k = obj.sigla
            posicao = ((ord(k[0]) + ord(k[1])) % 10 ) 
            self.ls_.inserir(self.lista_, obj, posicao)
            
    def imprimirTabela(self,):
        lista = []
        
        for i in range(0, len(self.lista_)):
            lista.clear()
            
            if self.lista_[i] == None:
                lista.append('None')
            else:    
                obj = self.lista_[i]
                lista.append(obj.sigla)
                while obj.proximo != None:
                    obj = obj.proximo
                    lista.append(obj.sigla)
                lista.append("None")
            
            print(f'{i}: ' + " -> ".join(lista))
        
#PROGRAMA PRINCIPAL:                    
t = tabelaHash()
print('TABELA HASH:\n')
t.funcHash('AC', 'Acre')
t.funcHash('AL', 'Alagoas')
t.funcHash('AP', 'Amapá')
t.funcHash('AM', 'Amazonas')
t.funcHash('BA', 'Bahia')
t.funcHash('CE', 'Ceará')
t.funcHash('DF', 'Distrito Federal')
t.funcHash('ES', 'Espírito Santo')
t.funcHash('GO', 'Goiás')
t.funcHash('MA', 'Maranhão')
t.funcHash('MT', 'Mato Grosso')
t.funcHash('MS', 'Mato Grosso do Sul')
t.funcHash('MG', 'Minas Gerais')
t.funcHash('PA', 'Pará')
t.funcHash('PB', 'Paraíba')
t.funcHash('PR', 'Paraná')
t.funcHash('PE', 'Pernambuco')
t.funcHash('PI', 'Piauí')
t.funcHash('RJ', 'Rio de Janeiro')
t.funcHash('RN', 'Rio Grande do Norte')
t.funcHash('RS', 'Rio Grande do Sul')
t.funcHash('RO', 'Rondônia')
t.funcHash('RR', 'Roraima')
t.funcHash('SC', 'Santa Catarina')
t.funcHash('SP', 'São Paulo')
t.funcHash('SE', 'Sergipe')
t.funcHash('TO', 'Tocantins')

#Estado Fictício:
t.funcHash('RM', 'Renan Maziero')

t.imprimirTabela()        