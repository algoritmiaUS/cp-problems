# Problem: Subordinates
# Solution by Kenny Jesús Flores Huamán
# url: https://cses.fi/problemset/task/1674b


import sys

sys.setrecursionlimit(200006)  # Aumenta el límite de recursión


def dfs(node, tree, subordinates):
    count = 0
    for child in tree[node]:
        count += dfs(child, tree, subordinates) + 1
    subordinates[node] = count
    return count


if __name__ == "__main__":
    n = int(input())
    ls = list(map(int, input().split()))

    tree = [[] for _ in range(n + 1)]
    subordinates = [0] * (n + 1)

    for idx, boss in enumerate(ls, start=2):
        tree[boss].append(idx)

    print(tree)
    dfs(1, tree, subordinates)

    output = subordinates[1:] 

    print(*output)