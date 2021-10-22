"""
Escreva um programa Python para verificar se uma determinada árvore binária é uma árvore binária completa ou não.
Para ser completa cada nó tem que possuir ou dois filhos ou nenhum
"""

arvore = [3,9,20,None, None, 15,7]

def verificaArvoreBinariaCompleta(lista):
    # retira a raiz 
    lista.pop(0)
    while len(lista) > 1:
        # varre a lista confirmando se aquele nó tem dois filhos ou não e deleta os nós da lista caso sim
        if (lista[0] == lista[1] == None) or (lista[0] != None and lista[1] != None):
            lista.pop(0)
            lista.pop(0)
        else:
            return False
    
    # se no final tiver sobrado algum elemento na lista significa que não é uma arvore completa
    if len(lista) > 0:
        return False
    else:
        return True

verificaArvoreBinariaCompleta(arvore)

############## utilizando classe
class NoArvore(object):
    def __init__(self, valor=0, nosFilhos=list()):
        self.valor = valor
        self.nosFilhos = nosFilhos
        
folha1 = NoArvore(1)
folha3 = NoArvore(3)
folha7 = NoArvore(7)
ramo2 = NoArvore(2, [folha1, folha3])
raiz = NoArvore(4, [ramo2, folha7])

def verificaArvoreBinariaCompletaClasse(no):
    if not (len(no.nosFilhos) == 0 or len(no.nosFilhos) == 2):
        return False
    else:
        if len(no.nosFilhos) > 0:
            retorno = verificaArvoreBinariaCompletaClasse(no.nosFilhos[0])
            if not retorno:
                return retorno
            retorno = verificaArvoreBinariaCompletaClasse(no.nosFilhos[1])
            if not retorno:
                return retorno
    return True

print(verificaArvoreBinariaCompletaClasse(raiz))


class NoArvoreBinaria(object):
    def __init__(self, valor=0, esquerda=None, direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def percorreArvore(no):
    if not no.esquerda and not no.direita:
        return True
    elif no.esquerda and no.direita:
        for filho in (no.esquerda, no.direita):
            valor = percorreArvore(filho)
            if not valor:
                return False
    else:
        return False
    return True




