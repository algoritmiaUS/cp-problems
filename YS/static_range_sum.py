# https://judge.yosupo.jp/problem/static_range_sum

N, Q = map(int, input().split())

prefix_sum = [0]
for num in input().split():
    prefix_sum.append(prefix_sum[-1] + int(num))


for _ in range(Q):
    a,b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a])


