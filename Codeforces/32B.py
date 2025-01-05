# Problem: Borze
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/32/B


borze = input()
n = len(borze)
number = []
i = 0

while i < n:
    if borze[i] == ".":
        number.append("0")
        i+=1
    else:
        if borze[i+1] == ".":
            number.append("1")
            i+=2
        else:
            number.append("2")
            i+=2

res = "".join(number)
print(res)