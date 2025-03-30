n = int(input())
t = list(map(int, input().split()))

res = list(filter(lambda x: x < 0, t))  
print(len(res)) 