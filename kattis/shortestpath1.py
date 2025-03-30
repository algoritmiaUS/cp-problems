#Solución por Kenny Jesús Flores Huamán
from heapq import heappush, heappop
import sys

INF = int(1e9)

def dijkstra(AL, s, n):
    """ Ejecuta Dijkstra desde el nodo `s` en un grafo de `n` nodos con 
    lista de adyacencia `AL`.
    """
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heappop(pq) 
        if d > dist[u]:
            continue 
        
        for v, w in AL[u]:
            if dist[u] + w < dist[v]:  
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    
    return dist

def leer_grafo_dirigido_ponderado(V, E):
    """Lee un grafo dirigido y ponderado."""
    AL = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        AL[u].append((v, w))  # Solo dirección u -> v con peso w
    return AL


first_case=True
while True:
    n, m, q, s = map(int, input().split())
    if n == 0 and m == 0 and q == 0 and s == 0:
        break

    AL = leer_grafo_dirigido_ponderado(n,m)

    D= dijkstra(AL,s,n)

    if not first_case:
            print()
    first_case = False

    for _ in range(q):
        x = int(input())
        if D[x] == INF:
            print("Impossible")
        else:
            print(D[x])