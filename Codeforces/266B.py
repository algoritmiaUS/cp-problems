# Problem: Queue at the School
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/266/B


n,t = map(int, input().split())
s = list(input())

for _ in range(t):
    i = 0
    while i < n - 1:
        if s[i] == "B" and s[i + 1] == "G":
            s[i], s[i + 1] = s[i + 1], s[i]
            i += 1
        i += 1 

res = "".join(s)
print(res)






