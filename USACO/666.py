import bisect
read = open("haybales.in", "r")
fout = open("haybales.out", "w")

N,Q = map(int, read.readline().split())
haybales = sorted(list(map(int, read.readline().split())))

for _ in range(Q):
    start, end = map(int, read.readline().split())
    res = bisect.bisect(haybales, end)- bisect.bisect(haybales, start-1)
    fout.write(f"{res}\n")



#  a,b,g = [int(x)-1 for x in read.readline().split()]

    
#     with open("shell.out", "w") as file:
#         file.write(str(max(counter))) 