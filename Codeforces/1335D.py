"""
Solution by Jesús Vílchez Martínez
"""

t = int(input())

for _ in range(t):
    sudoku_rows = []
    for _ in range(9):
        sudoku_rows.append([x for x in input().replace("2", "1")])

    
    for row in sudoku_rows:
        print(''.join(row))