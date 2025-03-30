#Solución por Kenny Jesús Flores Huamán
n,d = map(int, input().split())

ls = []
for i in range(n):
    ls.append(int(input()))

ls.sort()

records = []
temp = [ls[0]]
for i in range(1,len(ls)):
    temp.append(ls[i])
    if abs(temp[0]- temp[-1]) <= d:
        continue
    else:
        temp.pop()
        records.append(temp)
        temp=[ls[i]]

records.append(temp)
    
print(len(records))