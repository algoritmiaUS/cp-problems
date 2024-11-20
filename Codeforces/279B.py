n,t = map(int, input().split())
a = list(map(int, input().split()))


sum_acc = 0
left = 0
maximum=0

for right in range(n):
    sum_acc += a[right]
    while sum_acc > t:
        sum_acc-=a[left]
        left+=1    
    maximum = max(maximum, right-left+1)

print(maximum)