# Problem: Shell Game 
# Solution by Kenny Jesús Flores Huamán
# url: https://usaco.org/index.php?page=viewproblem2&cpid=891&lang=en

if __name__ == "__main__":
    read = open("shell.in")
    
    n = int(read.readline())

    shell_pos = [i for i in range(n)]
    counter = [0,0,0]

    for _ in range(n):
        a,b,g = [int(x)-1 for x in read.readline().split()]

        shell_pos[a], shell_pos[b] = shell_pos[b], shell_pos[a]

        counter[shell_pos[g]] +=1
    
    with open("shell.out", "w") as file:
        file.write(str(max(counter))) 
