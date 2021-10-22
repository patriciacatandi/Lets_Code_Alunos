"""
Grafo direcionado usando listas
https://www.youtube.com/watch?v=4-1fG04nQGI&list=PLrOyM49ctTx-xtyVeuO7ylclgXHd4ws9a&index=16
"""

class Grafo(object):
    def __init__(self, vertices:int) -> None:
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]# cada linha vai ser um vértice, mas não savemos a quantidade de arestas

    def adiciona_aresta(self, u, v):
        # aresta que sai do u e chega no v
        self.grafo[u-1].append(v)
        # self.grafo[v-1].append(u) para grafo não direcionado

    def mostra_lista(self):
        print("\nLinhas: \n")
        for i in range(self.vertices):
            print(f'{i+1}: ', end='   ')
           # print(self.grafo[i])
            for j in self.grafo[i]:
                print(f'{j}  ->', end='   ')
            print()

def isReachable(self, s, d):
    # Mark all the vertices as not visited
    visited =[False]*(self.V)

    # Create a queue for BFS
    queue=[]

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        #Dequeue a vertex from queue
        n = queue.pop(0)
            
        # If this adjacent node is the destination node,
        # then return true
        if n == d:
            return True

        #  Else, continue to do BFS
        for i in self.graph[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        # If BFS is complete without visited d
    return False

class Grafo_valorado(Grafo):
    def adiciona_aresta(self, u, v, peso):
        # aresta que sai do u e chega no v
        self.grafo[u-1].append([v, peso])


g = Grafo_valorado(4)

g.adiciona_aresta(1,2,3)
g.adiciona_aresta(1,3,2)
g.adiciona_aresta(1,4,4)
g.adiciona_aresta(3,4,3)
g.adiciona_aresta(2,3,1)

g.mostra_lista()

# g = Grafo(4)
# #g.mostra_lista()

# g.adiciona_aresta(1,2)
# g.adiciona_aresta(1,3)
# g.adiciona_aresta(1,4)
# g.adiciona_aresta(3,4)
# g.adiciona_aresta(2,3)

# g.mostra_lista()