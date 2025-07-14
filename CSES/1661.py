# https://cses.fi/problemset/task/1661
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0] * n
psum[0] = arr[0]

freq = {}

for i in range(1, n):
    psum[i] = psum[i - 1] + arr[i]
    freq[psum[i]] = 0

ans = 0
freq[0] = 1  # suma 0 antes de empezar

for asum in psum:
    ans += freq.get(asum - x, 0)
    freq[asum] = freq.get(asum, 0) + 1

print(ans)