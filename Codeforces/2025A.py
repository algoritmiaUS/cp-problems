# Problem: Two Screens
# Solution by Kenny Jesús Flores Huamán
# URL: https://codeforces.com/problemset/problem/2025A

def condicion(s: str, t: str, mid: int) -> bool:
    for k in range(len(s) + 1):  # Probar cada posible longitud de prefijo de s
        # Encontrar el mayor prefijo común entre s[:k] y t
        m = 0
        while m < len(t) and m < k and s[m] == t[m]:
            m += 1
        
        # Calcular el tiempo total:
        # 1. Escribir los primeros k caracteres de s
        # 2. Copiar esos k caracteres a la otra pantalla
        # 3. Escribir el resto de s y t
        total = k + 1 + (len(s) - k) + (len(t) - m)
        
        if total <= mid:
            return True
    return False


def solve(s:str,t:str) -> int:
    left, right = max(len(s), len(t)), 2*(len(s)+len(t))

    while left < right:
        # Tiempo que tardan las dos secuencias
        mid = (left+right) // 2

        # Si es posible completar las dos secuencias en mid segundos
        # Se intenta buscar un menor tiempo
        if condicion(s, t, mid):
            right = mid
        else:
            left = mid + 1

    # A veces puede ser que escribir cada pantalla uno por uno sea más rápido
    tt = len(s) + len(t)
    return left if tt > left else tt



if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        s = input()
        t = input()
        print(solve(s,t))