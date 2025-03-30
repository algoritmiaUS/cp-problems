#Solución por Kenny Jesús Flores Huamán

n = int(input())


# for op1 in ["+", "-", "*", "//"]:
#     for op2 in ["+", "-", "*", "//"]:
#         for op3 in ["+", "-", "*", "//"]:
#             expr_str = f"4 {op1.replace('//', '/')} 4 {op2.replace('//', '/')} 4 {op3.replace('//', '/')} 4"
#             expr_eval = f"4 {op1} 4 {op2} 4 {op3} 4"
#             result = eval(expr_eval)
#             dicc[result] = expr_str

#Este diccionario salió del código comentado
dicc = {16: '4 / 4 * 4 * 4', 8: '4 / 4 * 4 + 4', 24: '4 * 4 + 4 + 4', 9: '4 / 4 + 4 + 4', 0: '4 / 4 / 4 / 4', -8: '4 - 4 * 4 + 4', 7: '4 - 4 / 4 + 4', 68: '4 * 4 * 4 + 4', 1: '4 / 4 * 4 / 4', 4: '4 / 4 / 4 + 4', -16: '4 - 4 * 4 - 4', -1: '4 - 4 / 4 - 4', -60: '4 - 4 * 4 * 4', 32: '4 * 4 + 4 * 4', 17: '4 / 4 + 4 * 4', 15: '4 * 4 - 4 / 4', 60: '4 * 4 * 4 - 4', 256: '4 * 4 * 4 * 4', 2: '4 / 4 + 4 / 4', -7: '4 / 4 - 4 - 4', -15: '4 / 4 - 4 * 4', -4: '4 / 4 / 4 - 4'}


for _ in range(n):
    m = int(input())
    if m not in dicc:
        print("no solution")
    else:
        print(f"{dicc[m]} = {m}")