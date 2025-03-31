
def read_ints():
    return tuple(map(int, input().split()))


def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def solve(x, y, beepers, visited, startx, starty, mem):
    if len(visited) == len(beepers):
        return dist(x, y, startx, starty)

    visited_f = frozenset(visited)
    key = (x, y, visited_f)
    if key in mem:
        return mem[key]

    mini = float("inf")
    for i, (bx, by) in enumerate(beepers):
        if i in visited:
            continue

        visited.add(i)
        res = (
            dist(x, y, bx, by)
            + solve(bx, by, beepers, visited, startx, starty, mem)
        )
        visited.remove(i)

        if res < mini:
            mini = res

    mem[key] = mini
    return mini


t = int(input())
for _ in range(t):
    _, _ = read_ints()
    x, y = read_ints()
    n = int(input())
    beepers = [read_ints() for _ in range(n)]

    res = solve(x, y, beepers, set(), x, y, {})
    print(res)
