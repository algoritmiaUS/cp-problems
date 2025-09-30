def search(v):
    left = 0
    right = len(v) - 1

    while left < right:
        mid = (left + right) //2

        if v[mid] < v[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


def main():
    _ = input()
    v = list(map(int, input().split()))
    idx = search(v)
    print(idx)


if __name__ == "__main__":
    main()