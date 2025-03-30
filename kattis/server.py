n, T = map(int, input().split())
orders = list(map(int, input().split()))  # NO ordenar la lista
count = 0
acc = 0

for order in orders:
    if acc + order > T:
        print(count)
        break
    count += 1
    acc += order
else:
    print(count)
