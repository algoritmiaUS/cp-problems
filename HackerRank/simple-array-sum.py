# URL: https://www.hackerrank.com/challenges/simple-array-sum/problem

from typing import List

def solve(n:int, arr:List[int]) -> int:
    acc = 0
    for i in range(n):
        acc+=arr[i]
    return acc


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(" ")))
    res = solve(n,arr)
    print(res)