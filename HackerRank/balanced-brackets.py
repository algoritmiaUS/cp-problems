# Problem: Balanced Brackets
# URL: https://www.hackerrank.com/challenges/balanced-brackets/problem

n = int(input())

def solve(s:str) -> str:
    stack = []
    for bracket in s:
        if bracket in '{[(':
            stack.append(bracket)
        elif bracket == ")":
            if not stack or stack.pop() != "(":
                return "NO"
        elif bracket == "}":
            if not stack or stack.pop() != "{":
                return "NO"        
        elif bracket == "]":
            if not stack or stack.pop() != "[":
                return "NO"



    return "NO" if stack else "YES"
        
for _ in range(n):
    s = input()
    print(solve(s))