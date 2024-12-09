"""
Solution by Inés Dávila Herrero. C++ to Python 3 by Pablo Dávila Herrero.
URL: https://codeforces.com/problemset/problem/1419/D1
"""

n = int(input())
ls = list(map(int, input().split()))

ls.sort()

r = n // 2
if n % 2 == 0:
    r -= 1

print(r)

shift = n // 2
for i in range(n // 2):
    print(ls[i + shift], ls[i], end=" ")

if n % 2 == 1:
    print(ls[-1])
