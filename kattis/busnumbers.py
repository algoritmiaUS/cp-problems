n = int(input())
buses = list(map(int, input().split()))
buses.sort()

begin = end = buses[0]
output = [] 

for i in range(1, len(buses)):
    if buses[i] == end + 1:  # Es consecutivo
        end = buses[i]
    else:  # Se rompe la secuencia
        if end - begin >= 2:
            output.append(f"{begin}-{end}") 
        else:
            output.append(str(begin))
            if end != begin:
                output.append(str(end)) 

        begin = end = buses[i]  

if end - begin >= 2:
    output.append(f"{begin}-{end}")
else:
    output.append(str(begin))
    if end != begin:
        output.append(str(end))

print(" ".join(output))
