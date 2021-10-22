"""
è uma relação de agregação porque a classe CarrinhodeCompras
precisa da classe Produto, mas essa pode existir independente daquela

"""

from classes import CarrinhoDeCompras, Produto


prod1 = Produto('monitor', 800)
prod2 = Produto('mouse', 20)
prod3 = Produto('ddr2', 300)

car1 = CarrinhoDeCompras()
car1.inserir_produto(prod1)
car1.inserir_produto(prod2)
car1.inserir_produto(prod3)

car1.lista_produtos()
print(car1.soma_total())