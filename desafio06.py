# Desafio 01

# Crie uma função que retorna os vaores de duas listas
# de forma intercalada, mesmo quando as listas têm tamanho diferente.
# Por exemplo, dadas as listas:

import itertools


L1 = [1, 2, 3]
L2 = ["a", "b", "c", "d", "e"]

# Função deve retornar:

# [1, 'a', 2, 'b', 3, 'c', 'd', 'e']


def new_list():
    L3 = []
    for valor1, valor2 in itertools.zip_longest(L1, L2, fillvalue=None):
        if valor1 is not None:
            L3.append(valor1)
        if valor2 is not None:
            L3.append(valor2)
    return L3

L3 = new_list()
print(L3)