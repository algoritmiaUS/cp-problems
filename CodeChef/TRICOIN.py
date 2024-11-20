# Problem: Coins And Triangle
# URL: https://www.codechef.com/problems/TRICOIN

import math

def solve(n:int) -> int:

    return int(
        (-1+math.sqrt(1+8*n)) / 2
    )

T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))