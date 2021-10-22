class Cliente(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

# esse método é o responsável por criar a composição
    def insere_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
        
    def lista_enderecos(self):
        for end in self.enderecos:
            print("Printa endereço", end.cidade, end.estado)

class Endereco(object):
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

"""
To create the object we need a constructor method, __init__. 
The constructor can be used to set attributes of our object and 
perform any initialization routines.
"""