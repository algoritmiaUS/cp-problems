from math import sqrt, floor
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(floor((-1+(sqrt(1+(8*n))))/2))


if __name__ == "__main__":
    solve()