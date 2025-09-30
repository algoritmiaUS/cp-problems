
def solve():
    m,n = map(int, input().split())
    dicc = {}
    for _ in range(m):
        job, value = input().split()
        dicc[job]=value

    for _ in range(n):
        res = 0
        while True:
            line=input()
            if line==".":
                break
            
            words = line.split()
            for w in words:
                if w in dicc:
                    res+=int(dicc[w])
        print(res)

if __name__ == "__main__":
    solve()
            
