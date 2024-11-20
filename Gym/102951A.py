# Problem: Maximum Distance 
# URL: https://codeforces.com/gym/102951/problem/A

n = int(input())
x_coords =list(map(int,input().split()))
y_coords = list(map(int,input().split()))

max_distance = float('-inf')

for i in range(n):
    for j in range(1,n):
        distance = (x_coords[j]-x_coords[i])**2 + (y_coords[j]-y_coords[i])**2
        max_distance = max(max_distance, distance)

print(max_distance)