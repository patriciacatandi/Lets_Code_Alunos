"""
    Código para descobrir índices de pais e filhos da árvore
                        A
            B                       C
        D       E               F       G
"""

arvore = 'ABCDEFG'

def calcular_indice_filho_esquerdo(indice_pai):
    return (indice_pai + 1)*2 -1

def calcular_indice_filho_direito(indice_pai):
    return calcular_indice_filho_esquerdo(indice_pai) + 1

def calcular_indice_pai(indice_filho):
    return (indice_filho - 1)//2

print("Filhos esquerdos")
for i, v in enumerate(arvore):
    indice_filho_esquerdo = calcular_indice_filho_esquerdo(i)
    try:
        filho_esquerdo = arvore[indice_filho_esquerdo]
    except IndexError:
        print(f'{v} não tem filho')
    else:
        print(f'O filho esquerdo de {v} é {filho_esquerdo}')
        
print("\n\nFilhos direitos")
for i, v in enumerate(arvore):
    indice_filho_direito = calcular_indice_filho_direito(i)
    try:
        filho_direito = arvore[indice_filho_direito]
    except IndexError:
        print(f'{v} não tem filho')
    else:
        print(f'O filho direito de {v} é {filho_direito}')


print("\n\nPais")
for i, v in enumerate(arvore):
    indice_pai = calcular_indice_pai(i)
    if indice_pai == -1:
        print(f'{v} nao tem pai')
    else:
        pai = arvore[indice_pai]
        print(f'O pai de {v} é {pai}')


def calcular_altura_arvore(arvore):
    return len(arvore).bit_length() -1

print("Altura da árvore é ", calcular_altura_arvore(arvore))
 