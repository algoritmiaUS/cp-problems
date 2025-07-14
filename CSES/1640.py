# https://cses.fi/problemset/task/1640/
n,x = map(int, input().split())

arr = [(i + 1, int(num)) for i, num in enumerate(input().split())]
arr.sort(key=lambda x : x[1])
# print(arr)


def solve(arr, x):
    left, right = 0, len(arr) -1
    while left < right:
        current_sum = arr[left][1] +  arr[right][1]
        if current_sum == x:
            return f"{arr[left][0]} {arr[right][0]}"
        elif current_sum < x:
            left+=1
        else:
            right-=1

    return "IMPOSSIBLE"


print(solve(arr,x))