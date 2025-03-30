#Solución por Kenny Jesús Flores Huamán

import sys

low, high = 1, 1000
attempts = 10

for _  in range(attempts):
    mid = (low+ high) // 2
    print(mid)
    sys.stdout.flush()

    response = input().strip()
    if response == "correct":
        break
    elif  response == "lower":
        high  = mid-1
    elif response == "higher":
        low  = mid+1

    else:
        sys.exit()