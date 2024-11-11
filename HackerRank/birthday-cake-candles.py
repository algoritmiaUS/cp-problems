# Problem: Birthday Cake Candles
# Url: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

from typing import List
from collections import Counter

n = int(input())
candles = list(map(int, input().split()))

def solve(candles:List[int]) -> int:
    counter =  Counter(candles)
    return max(counter.items(), key=lambda t: t[1])[1]


print(solve(candles))
