"""
    https://www.youtube.com/watch?v=lA4UAIEGKaU&list=TLPQMTExMDIwMjHUPAg81Z4CWQ&index=2
    Associação é o link mais fraco entre classes, 
    pq se vc apaga o objeto escritor, os demais objetos não são apagados
"""

#from classes import Escritor, Caneta, MaquinaDeEscrever
from classes_modified import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# usa o método ferramenta como sendo a instancia maquina
escritor.ferramenta = maquina
# chama o metodo escrever da maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()

