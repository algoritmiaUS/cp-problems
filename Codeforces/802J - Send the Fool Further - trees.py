
import sys
from collections import defaultdict, deque

#################################
# Input
#################################

def leer_un_numero():
    return int(input().strip())

def leer_varios_numeros():
    return list(map(int, input().split()))

num_friends = leer_un_numero()
edges = [tuple(leer_varios_numeros()) for _ in range(num_friends - 1)]

#################################
# Construccion del arbol
#################################

tree_adj = defaultdict(list)
for u, v, c in edges:
    tree_adj[u].append((v, c))
    tree_adj[v].append((u, c))


#################################
# Algoritmo de resolucion
#################################

def bfs_farthest(n, start, tree_adj):
    """
    BFS modificado para encontrar el nodo más lejano desde un nodo dado en un árbol.

    Idea intuitiva:
    - Inicializamos una cola con el nodo de inicio y su distancia (0)
    - Extraemos un nodo de la cola y lo visitamos
    - Para cada vecino no visitado del nodo, lo visitamos y lo metemos
        en la cola con su distancia actualizada
    - Vamos repitiendo el proceso hasta que la cola esté vacía
    - Durante el proceso, vamos actualizando el nodo más alejado y la distancia máxima encontrada
    """
    # Inicialización
    visited = set()             # Nodos visitados
    visited.add(start)          # Partimos del nodo de inicio (visitado)
    farthest_node = start       # Nodo más alejado encontrado hasta el momento (inicialmente el nodo de inicio)
    max_dist = 0                # Distancia máxima encontrada hasta el momento (inicialmente 0)
    queue = deque([(start, 0)])  # Cola de BFS con (nodo, distancia acumulada)

    # Mientras haya nodos en la cola
    while queue:                       
        node, dist = queue.popleft()    # Extraemos un nodo de la cola

        if dist > max_dist:             # Si el nodo está más lejos que el nodo más lejano encontrado,
            max_dist = dist             # actualizamos la distancia máxima y el nodo más lejano
            farthest_node = node

        for neighbor, cost in tree_adj[node]:           # Metemos en la cola los vecinos no visitados del nodo
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + cost))

    return farthest_node, max_dist


#################################
# Output
#################################

farthest_from_0, distance = bfs_farthest(num_friends, 0, tree_adj)
print(distance)