class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    def ferramenta(self, ferramenta):
        self.ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.marca = marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')


"""
To create the object we need a constructor method, __init__. 
The constructor can be used to set attributes of our object and 
perform any initialization routines.
"""
