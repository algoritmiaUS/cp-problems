# Problem: Beautiful Year
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/271/A

y = int(input())+1

while True:
    if len(set(str(y))) == len(str(y)):
        print(y)
        break
    y+=1

