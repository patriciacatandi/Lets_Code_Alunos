"""
è uma relação de composição porque a classe Endereco é instanciada dentro de Cliente
aqui nem precisamos chamar a classe Endereço

"""

from classes import Cliente


cliente1 = Cliente('paty', 33)
cliente2 = Cliente('aline', 20)

cliente1.insere_enderecos('Sao Paulo', 'SP')
cliente1.insere_enderecos('Marilia', 'SP')

cliente2.insere_enderecos('Rio de Janeiro', 'RJ')

cliente1.lista_enderecos()