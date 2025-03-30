#Solución por Kenny Jesús Flores Huamán
a,b,c,n = map(int, input().split())


def solve(a,b,c,n):
    if (a+b+c) >= n and a>=1 and b>=1 and c>=1 and n>=3:
        return "YES"

    else:
        return "NO"

print(solve(a,b,c,n))