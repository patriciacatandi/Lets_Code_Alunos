"""
Criar um grafo direcionado simples (sem arestas paralelas)
"""

class Grafo(object):
    def __init__(self, vertices:int) -> None:
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)] # cria matrix de teamanho vertice x vertice

    def adiciona_aresta(self, u:int, v:int):
        self.grafo[u-1][v-1] = 1 # se for possível arestas paralelas trocar o = por += (grafo múltiplo)
        # se fosse um grafo não direcionado precisaríamos criar o [v,u]:
        #self.grafo[v-1, u-1] = 1
    
    def mostra_matriz(self):
        print("\nMatriz: \n")
        for i in range(self.vertices):
            print(self.grafo[i])

class MatrizDistancia(Grafo):
    """
    Vamos considerar pesos para as arestas
    """
    def adiciona_aresta(self, u:int, v:int, peso:float):
        self.grafo[u-1][v-1] = peso



# Usuário fornece arestas
v = int(input("Digite a quantidade de vertices: "))
g = MatrizDistancia(v)

a = int(input("Digite a qnt de arestas: "))
for i in range(a):
    u = int(input("De qual vértice parte essa aresta: "))
    v = int(input("Para qual vértice chega essa aresta: "))
    p = int(input("Qual o peso dessa aresta: "))
    g.adiciona_aresta(u, v, p)

# g = MatrizDistancia(4)
# g.mostra_matriz()

# g.adiciona_aresta(1,2,5)
# g.adiciona_aresta(3,4,3)
# g.adiciona_aresta(2,3,9)

g.mostra_matriz()

# g = Grafo(4)
# g.mostra_matriz()

# g.adiciona_aresta(1,2)
# g.adiciona_aresta(3,4)
# g.adiciona_aresta(2,3)

# g.mostra_matriz()

