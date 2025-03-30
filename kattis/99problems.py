#Solución por Kenny Jesús Flores Huamán
N = int(input())
numbers = [(abs(n-N),n) for n in range(1, 10001) if n % 100 == 99]
print(min(numbers, key=lambda x: (x[0], -x[1]))[1])
