
class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendedor = None
        self.comprador = None  

class Pessoa():
    def __init__(self, nome, cpf):
       self.nome = nome
       self.cpf = cpf

class Venda():
    def __init__(self, num_nf, veiculo, comprador, vendedor, valor):
        self.nf=num_nf
        self.veiculo = veiculo
        self.comprador = comprador
        self.vendedor = vendedor
        self.valor = valor    

veiculo = Veiculo('P.G-207', 2007, 25000)
comprador = Pessoa('Rodrigo','05063499180')
vendedor = Pessoa('João','099634996690')
venda = Venda('18-450', veiculo, comprador, vendedor, 30000)

print('Dados da venda:')
print('NF: '+venda.nf, 'Veiculo: '+venda.veiculo.modelo+'/'+str(venda.veiculo.ano), 
'Comprador: '+venda.comprador.nome, \
  'Vendedor: '+venda.vendedor.nome, 'Valor: '+str(venda.valor), sep='\n')
