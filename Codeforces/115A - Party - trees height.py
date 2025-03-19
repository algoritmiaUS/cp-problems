import sys
from collections import defaultdict, deque

#################################
# Input
#################################

def leer_un_numero():
    return int(sys.stdin.readline().strip())

def leer_varios_numeros(n):
    return [int(sys.stdin.readline().strip()) for _ in range(n)]

sys.setrecursionlimit(3000)         # Evitar errores de límite de recursión

n = leer_un_numero()
managers = leer_varios_numeros(n)


#################################
# Resolución del problema
#################################

def iterative_dfs(root, tree):
    """
    Calcula la profundidad máxima de un árbol usando DFS iterativo.
    """
    stack = [(root, 1)]  # (nodo_actual, profundidad)
    max_depth = 1

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        for subordinate in tree[node]:
            stack.append((subordinate, depth + 1))

    return max_depth

def find_max_depth(n, managers):
    """
    Calcula la máxima profundidad del árbol organizacional basado en la jerarquía de los managers.
    """
    # Construcción del árbol como lista de adyacencia
    tree = defaultdict(list)
    roots = []

    for employee in range(n):
        manager = managers[employee]
        if manager == -1:
            roots.append(employee + 1)  # Convertir a índice basado en 1
        else:
            tree[manager].append(employee + 1)  # Almacenar subordinados

    # Determinar la máxima profundidad entre todas las raíces
    max_group_count = 0
    for root in roots:
        max_group_count = max(max_group_count, iterative_dfs(root, tree))

    return max_group_count


#################################
# Output
#################################

print(find_max_depth(n, managers))
