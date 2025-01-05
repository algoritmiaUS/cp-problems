# Problem: Beautiful Matrix
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/263/A


n = 5 # 5x5

matrix = []

for _ in range(n):
    ls = list(map(int,input().split()))
    matrix.append(ls)


for row in range(n):
    for col in range(n):
        if matrix[row][col] == 1:
            # P1 = (x1,y1) Punto donde está el 1
            # P2 = (3,3) Punto donde está el medio, y es donde queremos poner el 1
            x1 = row+1
            y1 = col+1
            distance = abs(x1-3) + abs(y1-3) # Distancia Manhattan |x1 - x2| + |y1 - y2|
            print(distance)
            break
