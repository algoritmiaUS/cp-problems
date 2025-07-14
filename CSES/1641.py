# https://cses.fi/problemset/task/1641

n,x = map(int, input().split())
arr = [(i + 1, int(num)) for i, num in enumerate(input().split())]
arr.sort(key=lambda x : x[1])


def solve(arr, x):
    if len(arr) < 3:
        return "IMPOSSIBLE"

    for i in range(n):
        target = x - arr[i][1]
        first_idx = arr[i][0]
        left, right = i+1, len(arr)-1
        while left < right:
            current_sum = arr[left][1] +  arr[right][1]
            if current_sum == target:
                res = sorted([arr[left][0], first_idx, arr[right][0]])
                return f"{res[0]} {res[1]} {res[2]}"
            elif current_sum < target:
                left +=1
            else:
                right-=1



    return "IMPOSSIBLE"


print(solve(arr, x))