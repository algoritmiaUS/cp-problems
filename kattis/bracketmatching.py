#Solución por Kenny Jesús Flores Huamán
def solve(s: str) -> str:
    stack = []
    valid_brackets = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in valid_brackets.values():  # Si es un paréntesis de apertura
            stack.append(c)
        elif c in valid_brackets:  # Si es un paréntesis de cierre
            if stack and stack[-1] == valid_brackets[c]:
                stack.pop()
            else:
                return "Invalid"

    return "Valid" if not stack else "Invalid"
_ =  input()
s = input()

print(solve(s))