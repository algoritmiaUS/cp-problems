# F - Trouble Sort
"""
Solution by Pablo Moreno Moreu

"""

def lee_numero():
    return int(input())

def lee_lista():
    return list(map(int, input().split()))


def solve(vals, tipos):
    # so long as you have an element of each type, you can do it
    if len(set(tipos))>1:
        print('YES')
        return
    # if you only have one type, it needs to be sorted
    else:
        s_vals = sorted(vals)
        if vals==s_vals:
            print('YES')
            return
        else:
            print('NO')
            return
    pass

if __name__ == '__main__':
    n = lee_numero()
    while n>0:
        lee_numero()
        vals = lee_lista()
        tipos = lee_lista()
        solve(vals, tipos)
        n-=1