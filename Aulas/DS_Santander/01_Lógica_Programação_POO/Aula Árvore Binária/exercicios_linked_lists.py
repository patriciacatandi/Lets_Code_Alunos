
class No(object):
    '''
    Cria nós
    '''
    def __init__(self, valor) -> None:
        self.valor = valor
        self.direita = None

    def obtervalor(self):
        return self.valor

    def setdireita(self, direita):
        self.direita = direita

    def obterdireita(self):
        return self.direita

def print_elements(actual):
    '''
    printa elementos a partir do nó actual
    '''
    curr = actual.obterdireita()
    print(actual.obtervalor())
    while curr:
        print(curr.obtervalor())
        curr = curr.obterdireita()

def insert_node_at_tail(actual, element):
    '''Insert a Node at the Tail of a Linked List
    varrer linked lista até encontrar obterdireita None'''
    curr = actual.obterdireita()
    while curr.obterdireita():
        #print(curr.obtervalor())
        curr = curr.obterdireita()
    else:
        curr.setdireita(No(element))

def insert_node_at_head(actual, element):
    """
    Insert a node at the head of a linked list
    Considerando que vc passa o primeiro elemento da lista
    """
    no0 = No(element)
    no0.setdireita(actual)
    return no0

def insert_node_at_position(actual, element, position):
    '''Insert a Node at a especific location in a Linked List
    varrer linked lista até encontrar a posiçao
    atribui o que estava à direita para ser o direita desse novo nó
    atribui esse novo nó como à direita do anterior
    '''
    curr = actual
    for i in range(position-1):
        curr = curr.obterdireita()
    node = No(element)
    # atribui o valor atual à direita pra o novo node
    node.setdireita(curr.obterdireita())
    # seta o novo node como a direita desse que pausamos
    curr.setdireita(node)


def get_elements(actual):
    '''
    printa elementos a partir do nó actual
    '''
    all_elements = [actual.obtervalor()]
    curr = actual.obterdireita()
    while curr:
        all_elements.append(curr.obtervalor())
        curr = curr.obterdireita()
    return all_elements

def delete_node(actual, position):
    pass

"""
àrvore:
            4 ->  2 -> 5  -> 7  -> 10
"""
# cria nós
no1 = No(4)
no2 = No(2)
no3 = No(5)
no4 = No(7)
no5 = No(10)

# cria dependência ou linked list lista encadeada
no1.setdireita(no2)
no2.setdireita(no3)
no3.setdireita(no4)
no4.setdireita(no5)

#print(no1.obtervalor())
#print(no1.obterdireita().obtervalor()) # assim conseguimos acessar o filho à direita do nó 1
#print(no2.obterdireita().obtervalor())


# adicionar elemento no fim
insert_node_at_tail(no1, 11)

# adicionar elemento no inicioa
no0 = insert_node_at_head(no1, 0)

# printar todos os elementos
print_elements(no0)

#adiciona elemento na posição position
insert_node_at_position(no0, 99, 4)

# traz todos os elementos
all_elements = get_elements(no0)
print(all_elements)