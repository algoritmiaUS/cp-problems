
case_count = 1

while True:
    try:
        line = input().split()
        x = float(line[0])
        y = float(line[1])
        r = int(line[2])
        c = complex(x,y)
        z = complex(0,0)
        diverged = False
        for it in range(r):
            z = (z*z) + c
            if abs(z) > 2: 
                diverged = True
                break
        
        if diverged:
            print(f"Case {case_count}: OUT")
        else:
            print(f"Case {case_count}: IN")
        case_count+=1
    except EOFError:
        break