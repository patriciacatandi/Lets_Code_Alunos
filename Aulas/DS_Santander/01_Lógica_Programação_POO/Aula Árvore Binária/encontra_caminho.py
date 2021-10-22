'''
https://www.python.org/doc/essays/graphs/
'''

def find_path(graph, start, end, path=[]):
        path = path + [start]
        print('path', path)
        if start == end:
            return path
        #if not graph.has_key(start):
        #    return None
        for node in graph[start]:
            print("Buscando no nó: ", start)
            print('we are on node ', node)
            if node not in path:
                print('entra na recursão')
                newpath = find_path(graph, node, end, path)
                if newpath: 
                    return newpath
        return None


def dfs(grafo, verticeA, verticeB, visitados = list(), caminho = list()):
    """
    codigo brian
    """
    visitados.append(verticeA)
    caminho.append(verticeA)
    if verticeA == verticeB:
        return caminho
    for vizinho in grafo[verticeA]:
        if vizinho not in visitados:
            rota = dfs(grafo, vizinho, verticeB, visitados, caminho)
            if rota != None:
                return rota
            caminho.pop()

# original
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['E','D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

"""
Grafo utilizado na aula do Brian
0  ->  1  ->  3 -> 4 -> 5 -> 7 -> 6 
       ^           ^^             |     
       |           ||             |
       2  -->------  ------<-------
"""
graph_num = [
    [1],
    [3],
    [1],
    [2, 4],
    [5],
    [7],
    [4],
    [6]
]
print('find path')
#a = find_path(graph, 'A', 'D')
a = find_path(graph_num, 1, 6)
print(a)    #['A', 'B', 'C', 'D']




def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        #if not graph.has_key(start):
        #    return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

print(find_all_paths(graph, 'A', 'D'))
    #[['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        #if not graph.has_key(start):
        #    return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

print('find_shortest_path')
print(find_shortest_path(graph, 'A', 'D'))
#    ['A', 'C', 'D']


