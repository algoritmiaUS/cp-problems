# Problem: Queries about less or equal elements
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/600/B

n, m = map(int,input().split()) # a,b
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def binary_search(numbers, target):
    left, right = 0, len(numbers)-1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] <=  target:
            left = mid+1
        else:
            right = mid -1

    return left
a.sort()
res = []
for bj in b:
    count = binary_search(a, bj)
    res.append(count)


print(" ".join(map(str, res)))

