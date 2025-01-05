# Problem: Young Physicist
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/69/A

n = int(input())

x,y,z = 0,0,0

for _ in range(n):
    xi,yi,zi = map(int, input().split())
    x+=xi
    y+=yi
    z+=zi

print("YES" if x ==0 and y==0 and z==0 else "NO")
