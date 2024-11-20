# Problem: osu!mania
# URL: https://codeforces.com/problemset/problem/2009/B

t= int(input())
for _ in range(t):
    sol = []
    n = int(input())
    for _ in range(n):
        pos = input().index("#")+1
        sol.append(pos)
    
    print(" ".join(map(str, sol[::-1])))
