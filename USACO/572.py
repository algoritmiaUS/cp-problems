# https://usaco.org/index.php?page=viewproblem2&cpid=572

with open("bcount.in", "r") as fin:
    N, Q = map(int, fin.readline().split())

    prefix_sum = [[0, 0, 0]]  # Inicialización para vacas de tipo 1, 2 y 3

    for _ in range(N):
        num = int(fin.readline())
        a, b, c = prefix_sum[-1]
        temp = [0, 0, 0]
        temp[num - 1] = 1  # Ajustamos índice para 0-based
        prefix_sum.append([a + temp[0], b + temp[1], c + temp[2]])

    queries = [tuple(map(int, fin.readline().split())) for _ in range(Q)]

with open("bcount.out", "w") as fout:
    for a, b in queries:
        h = prefix_sum[b][0] - prefix_sum[a - 1][0]
        g = prefix_sum[b][1] - prefix_sum[a - 1][1]
        j = prefix_sum[b][2] - prefix_sum[a - 1][2]
        fout.write(f"{h} {g} {j}\n")