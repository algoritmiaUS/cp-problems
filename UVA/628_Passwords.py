# Problem: Passwords
# Solution by Kenny Jesús Flores Huamán
# url: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=569


def solve(dictionary, rule, password, index):
    # Caso Base
    if len(rule) == index:
        print(password)
        return 

    c =  rule[index]
    if c == "#":
        for word in dictionary:
            solve(dictionary, rule, password + word, index + 1)
    elif c== "0":
        for num in range(10):
            solve(dictionary, rule, password + str(num), index + 1)


if __name__ == "__main__":

    while True:
        try: 
            n = int(input())
            words = [input() for _ in range(n)]
            n_rules = int(input())
            rules = [input() for _ in range(n_rules)]
            print("--")
            for rule in rules:
                solve(words, rule, "", 0)

        except EOFError:
            break
    

