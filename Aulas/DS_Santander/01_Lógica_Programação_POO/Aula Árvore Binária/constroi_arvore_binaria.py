
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

"""
àrvore:
            4
        2       5
"""
no1 = No(4)
no2 = No(2)
no3 = No(5)

print(no1.obtervalor())
print(no1.obterdireita())

no1.set_esquerda(no2)
no1.set_direita(no3)

print(no1.obterdireita()) # esse aqui retorna ( o endereço) a posição do objeto na memória
print(no1.obterdireita().obtervalor()) # assim conseguimos acessar o filho à direita do nó 1