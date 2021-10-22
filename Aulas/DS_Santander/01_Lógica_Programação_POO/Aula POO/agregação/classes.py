class CarrinhoDeCompras(object):
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for prod in self.produtos:
            print(f"Produto {prod.nome} custa {prod.valor}")

    def soma_total(self):
        total = 0
        for prod in self.produtos:
            total += prod.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


"""
To create the object we need a constructor method, __init__. 
The constructor can be used to set attributes of our object and 
perform any initialization routines.
"""
