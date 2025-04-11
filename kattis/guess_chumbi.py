"""
Problem: Guess the Number
URL: https://open.kattis.com/problems/guess

Solution by Pablo Dávila Herrero (https://pablodavila.eu)
"""

a = 1
b = 1_001
while True:
    n = (a+b) // 2
    print(n)
    ans = input()

    if ans == "lower":
        b = n
    elif ans == "higher":
        a = n+1
    else:
        break
