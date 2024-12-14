"""
Solution by Pablo Dávila Herrero.
URL: https://codeforces.com/problemset/problem/1486/C1
"""


# # Random test case generation for debugging

# c = 0
# while True:
#     c += 1

#     import random
#     actual_list = list(range(random.randrange(2, 100)))
#     random.shuffle(actual_list)
#     answer = actual_list.index(max(actual_list)) + 1
#     # print("answer", answer)

#     def query(i, j):
#         # print(f"q {i=}, {j=}", flush=True)
#         ls = actual_list[i-1:j]
#         if len(ls) == 1:
#             return ls[0]
#         second_greatest = sorted(ls)[-2]
#         return actual_list.index(second_greatest)+1

#     n = len(actual_list)

#     second = query(1, n)
#     if second != 1:
#         left_test = query(1, second)

#         if left_test == second:
#             i = 1
#             j = second + 1
#             left_side = True
#         else:
#             i = second
#             j = n + 1
#             left_side = False
#     else:
#         right_test = query(second, n)

#         if right_test == second:
#             i = second
#             j = n + 1
#             left_side = False
#         else:
#             i = 1
#             j = second + 1
#             left_side = True

#     while j - i > 2:
#         m = (i + j) // 2
#         # print(f"{i=}, {j=}, {m=}")

#         if left_side:
#             test = query(m, second)
#             if test == second:
#                 i = m
#             else:
#                 j = m

#         else:
#             test = query(second, m)
#             if test == second:
#                 j = m + 1
#             else:
#                 i = m + 1

#     if j - i == 2:
#         # print(i,j)
#         if i == second:
#             i += 1
#         elif i+1 == second:
#             pass
#         elif left_side:
#             if query(i+1, second) == second:
#                 i += 1
#         elif query(second, i) != second:
#             i += 1 

#     # print("!", i, flush=True)

#     if i != answer:
#         print("Wrong answer")
#         print("Expected:", answer)
#         print("Got:", i)
#         print("List:", actual_list)
#         print("Second:", second)
#         print("Left test:", left_test)
#         print("Left side:", left_side)
#         print("Left:", i)
#         print("Right:", j)

#         break

#     print(c)


# The actual solution

def query(i, j):
    print("?", i, j, flush=True)
    return int(input())


n = int(input())

second = query(1, n)
if second != 1:
    left_test = query(1, second)

    if left_test == second:
        i = 1
        j = second + 1
        left_side = True
    else:
        i = second
        j = n + 1
        left_side = False
else:
    right_test = query(second, n)

    if right_test == second:
        i = second
        j = n + 1
        left_side = False
    else:
        i = 1
        j = second + 1
        left_side = True

while j - i > 2:
    m = (i + j) // 2

    if left_side:
        test = query(m, second)
        if test == second:
            i = m
        else:
            j = m

    else:
        test = query(second, m)
        if test == second:
            j = m + 1
        else:
            i = m + 1

if j - i == 2:
    if i == second:
        i += 1
    elif i+1 == second:
        pass
    elif left_side:
        if query(i+1, second) == second:
            i += 1
    elif query(second, i) != second:
        i += 1 

print("!", i, flush=True)
