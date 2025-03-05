from collections import deque

tallas = ["XS", "S", "M", "L", "XL", "XXL"]
talla_idx = {t: i for i, t in enumerate(tallas)}

#################################
# Input
#################################

def leer_un_numero():
    return int(input().strip())

def leer_varios_numeros():
    return list(map(int, input().split()))

def leer_solicitudes(m):
    return [input().strip().split() for _ in range(m)]

test_cases = leer_un_numero()
problemas = []
for _ in range(test_cases):
    N, M = leer_varios_numeros()
    solicitudes = leer_solicitudes(M)
    problemas.append((N, M, solicitudes))

#################################
# Grafo
#################################

def construir_grafo(N, M, solicitudes):
    camisetas_por_talla = N // 6  # Todas las tallas tienen la misma cantidad de camisetas

    # Nodos: 6 tallas + M voluntarios + fuente + sumidero
    V = 6 + M + 2  
    source, sink = V - 2, V - 1  

    # Grafo como matriz de adyacencia 
    graph = {i: {} for i in range(V)}

    # Adyacencias
    for i in range(6):  # Fuente -> tallas, peso = número de camisetas
        graph[source][i] = camisetas_por_talla
        graph[i][source] = 0

    for i, (t1, t2) in enumerate(solicitudes):
        participant_node = i + 6
        graph[talla_idx[t1]][participant_node] = 1  # Participante -> talla que acepta
        graph[participant_node][talla_idx[t1]] = 0
        graph[talla_idx[t2]][participant_node] = 1
        graph[participant_node][talla_idx[t2]] = 0
        graph[participant_node][sink] = 1  # Participante -> sumidero
        graph[sink][participant_node] = 0

    return graph, source, sink

#################################
# Funciones del Algoritmo (Edmonds-Karp)
#################################

def bfs(graph, source, sink, parent):
    queue = deque([source])
    visited = set([source])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                parent[v] = u
                visited.add(v)
                if v == sink:
                    return True
                queue.append(v)
    return False

def send_flow(graph, source, sink):
    parent = {}
    if not bfs(graph, source, sink, parent):
        return 0

    v, path_flow = sink, float('inf')
    while v != source:
        u = parent[v]
        path_flow = min(path_flow, graph[u][v])
        v = u

    v = sink
    while v != source:
        u = parent[v]
        graph[u][v] -= path_flow
        graph[v][u] += path_flow
        v = u

    return path_flow

def edmonds_karp(graph, source, sink):
    flow = 0
    while True:
        sent_flow = send_flow(graph, source, sink)
        if sent_flow == 0:
            break
        flow += sent_flow
    return flow

#################################
# Output
#################################

for N, M, solicitudes in problemas:
    graph, source, sink = construir_grafo(N, M, solicitudes)
    max_flow = edmonds_karp(graph, source, sink)
    print("YES" if max_flow == M else "NO")