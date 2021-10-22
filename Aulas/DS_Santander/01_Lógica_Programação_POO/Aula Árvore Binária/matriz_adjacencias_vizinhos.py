def adjacent_nodes(matriz, node_1, node_2):
    if matriz[node_1][node_2]==1:
        return True
    else:
        return False

ma = [
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

print('0 e 1', adjacent_nodes(ma, 0, 1))
print('0 e 2', adjacent_nodes(ma, 0, 2))