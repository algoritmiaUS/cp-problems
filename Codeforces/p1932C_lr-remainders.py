"""
Problem: 1932/C - LR-remainders
URL: https://codeforces.com/problemset/problem/1932/C

Solution by Pablo Dávila Herrero (https://pablodavila.eu)
"""

# # TLE solution (T(n) = 3*n -> O(n))
# t = int(input())
# for _ in range(t):
#     n, m = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     b = list(input())

#     sorted_a = []
#     for l in b:
#         if l == 'L':
#             sorted_a.append(a.pop(0))
#         else:
#             sorted_a.append(a.pop())
    
#     results = []
#     res = 1
#     for e in reversed(sorted_a):
#         res = (res * e) % m
#         results.append(res)

#     # print(*results)
#     print("OUT:", *reversed(results))  # TEMP


# AC solution (T(n) = 2*n -> O(n))
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(input())

    left = n-1
    for i in range(n-1):
        if b[i] == "R":
            left -= 1
    right = left

    res = a[left] % m
    results = [res]
    for l in b[-2::-1]:
        if l == "L":
            left -= 1
            res = (res * a[left]) % m
        else:
            right += 1
            res = (res * a[right]) % m

        results.append(res)

    print(*reversed(results))
    # print("OUT:", *reversed(results))  # TEMP
