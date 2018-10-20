# DAILY CODE MODE
# symbol = "*"
# n = 4
#
# print(symbol + " : " + " ".join([str(x) for x in range(n)]))
# answer = []
# for i in range(n + 1):
#     answer.append([str(i) + " : "])
#     for j in range(n + 1):
#         if symbol == "+":
#             answer[i].append(str(i + j))
#         elif symbol == "-":
#             answer[i].append(str(i - j))
#         elif symbol == "*":
#             answer[i].append(str(i * j))
#     print(" ".join(answer[i]))
#
# Answer by Say_What1
# def c98(op, n):
#     n = int(n)
#     table = [[0]*(n+1) for i in range(n+1)]
#     div = ''
#     run = [i for i in range(n+1)]
#     for i in range(n+1):
#         div += '----'
#         for j in range(n+1):
#              table[i][j] = eval('%d%s%d'%(i, op, j))
#     print(op,'|', str(run).strip('[]').replace(',',' '))
#     print(div)
#     for i in run:
#         print(run[i], '|', str(table[i]).strip(',[]').replace(',', ' '))
# c98('+',4)
#
# BREAKDOWN
# table[i][j] = eval('%d%s%d'%(i, op, j))
#
# str(run).strip('[]').replace(',',' '))
# It seems that this is just a way of joining up a list with a space between each block which we would usually do with " ".join(given_list)
#
# SUMMARY
# Another easy one, this is easy enough to do and just requires nested looping. Not so sure about the given answer as it repeats a lot of steps in a cumbersome way.
#
