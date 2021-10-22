### https://www.youtube.com/watch?v=LVU82pzi938&list=PLrOyM49ctTx-xtyVeuO7ylclgXHd4ws9a&index=24

class No(object):
    def __init__(self, valor) -> None:
        self.valor = valor
        self.esquerda = None
        self.direita = None
        #super().__init__()

    def obtervalor(self):
        return self.valor

    def set_esquerda(self, esquerda):
        self.esquerda = esquerda

    def set_direita(self, direita):
        self.direita = direita

    def obteresquerda(self):
        return self.esquerda

    def obterdireita(self):
        return self.direita


class ArvoreBinariaBusca:
    def __init__(self) -> None:
        self.raiz = None

    def obter_raiz(self):
        return self.raiz

    def insere(self, valor):
        no = No(valor)
        # achar o pai dele para adicoinar ma esquerda ou direita
        if self.raiz == None:
            self.raiz = no
            #print('criou raiz', self.raiz.obtervalor())
        else:
            no_atual = self.raiz
            no_pai = None
            while True:
                #print(no_atual.obtervalor())
                if no_atual != None:
                    no_pai = no_atual
                    if no.obtervalor() < no_atual.obtervalor():
                        #print(no_atual.obtervalor(), no.obtervalor())
                        no_atual = no_atual.obteresquerda()
                        #print('esquerda', no_atual)
                    else:
                        no_atual = no_atual.obterdireita() 
                        #print('direita', no_atual) 
                else: 
                    if no.obtervalor() < no_pai.obtervalor():
                        no_pai.set_esquerda(no)
                    else: 
                        no_pai.set_direita(no)  
                    break

    def mostra_arvore(self, no_atual): # percurso em ordem simétrica
        if no_atual != None:
            self.mostra_arvore(no_atual.obteresquerda())
            print(f'{no_atual.obteresquerda()}', end='  ')
            self.mostra_arvore(no_atual.obterdireita())

"""
                8
        3               10
   1        6                14
          4   7           11  

"""
#{8,3,6,10,14,1,7,13,4}
t = ArvoreBinariaBusca()
t.insere(8)
t.insere(3)
t.insere(6)
t.insere(10)
t.insere(14)
t.insere(1)
t.insere(7)
t.insere(13)
t.insere(4)

t.mostra_arvore(t.obter_raiz())
#  a ordem em percurso simétrico tem que ser {1,3,4,6,7,8,10,13,14}

