#Solución por Kenny Jesús Flores Huamán

import sys

input = sys.stdin.readline
INF = int(1e9)

def leer_grafo_floyd(V, E):
    """
    Si |V| > 450, no deberías emplear Floyd-Warshall debido a su complejidad O(n^3).
    """
    AM = [[INF] * V for _ in range(V)]
    for u in range(V):
        AM[u][u] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        AM[u][v] = min(AM[u][v], w)  # Manejo de múltiples aristas
    return AM

def floyd_warshall(AM, V):
    """
    Ejecuta el algoritmo de Floyd-Warshall para encontrar las distancias mínimas
    entre todos los pares de vértices en un grafo representado por su matriz de adyacencia.
    """
    for k in range(V):
        for u in range(V): 
            for v in range(V):
                if AM[u][k] < INF and AM[k][v] < INF:  # Evita desbordamiento con INF
                    AM[u][v] = min(AM[u][v], AM[u][k] + AM[k][v])

    return AM

first_case = True
while True:
    n, m, q = map(int, input().split())
    if n == 0 and m == 0 and q == 0:
        break

    AM = leer_grafo_floyd(n, m)
    result = floyd_warshall(AM, n)

    if not first_case:
        print()
    first_case = False

    for _ in range(q):
        u, v = map(int, input().split())
        if u == v:
            if result[u][u] < 0:  # Ciclo negativo en u
                print("-Infinity")
            else:
                print(0)
        elif result[u][v] == INF:
            print("Impossible")
        elif any(result[i][i] < 0 and result[u][i] < INF and result[i][v] < INF for i in range(n)):
            print("-Infinity")  # Detectar ciclos negativos que afectan u -> v
        else:
            print(result[u][v])
