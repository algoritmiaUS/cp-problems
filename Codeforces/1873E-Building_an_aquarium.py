def main():
    tests_number = int(input())
    for _ in range(tests_number):
        n,x = map(int,input().split())
        corals = sorted(list(map(int,input().split())))
        h = corals[-1]
        water = sum(map(lambda i:max(h-i,0),corals))
        if water<=x:
            print((x-water)//n+h)
            continue
        b = h
        last_b = b
        a = 0
        last_a = a
        h = (b-a)//2
        while True:
            water = sum(map(lambda i:max(h-i,0),corals))
            if water>x:
                b = (a+b)//2
            else:
                a = (a+b)//2
            if last_b==b and last_a==a:
                h+=1
                if sum(map(lambda i:max(h-i,0),corals))<=water:
                    print(h)
                    break
                print(h-1)
                break
            last_b = b
            last_a = a
            h = (a+b)//2

if __name__=="__main__":
    main()
