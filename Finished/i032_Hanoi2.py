# T = [[7, 6, 5, 4, 3, 2, 1], [], []]
# source = 0; spare = 1; destination = 2;
# lastPlayedNum = 1; lastplayedPos = source
#
# def toMove(lastPlayed):
#     cho = [0, 1, 2]
#     cho.pop(lastPlayed)
#     if len(T[cho[1]]) == 0:
#         return cho[0]
#     if len(T[cho[0]]) == 0:
#         return cho[0]
#     if T[cho[1]][-1] > T[lastPlayed][-1] and T[cho[0]][-1] < T[lastPlayed][-1]:
#         return cho[0]
#     if T[cho[1]][-1] < T[lastPlayed][-1] and T[cho[0]][-1] > T[lastPlayed][-1]:
#         return cho[1]
#     if T[cho[1]][-1] > T[lastPlayed][-1] and T[cho[0]][-1] > T[lastPlayed][-1]:
#         if T[cho[0]][-1] > T[cho[1]][-1]:
#             return cho[1]
#         else:
#             return cho[0]
# def moveWhere(mover):
#     cho = [0, 1, 2]
#     cho.pop(mover)
#     if T[mover][-1] == 1:
#         if T[cho[0]][-1] %2 == 0:
#             return cho[0]
#         else:
#             return cho[1]
#     if len(T[cho[0]]) == 0:
#         return cho[0]
#     if len(T[cho[1]]) == 0:
#         return cho[1]
#     if T[cho[1]][-1] > T[mover][-1] and T[cho[0]][-1] < T[mover][-1]:
#         return cho[1]
#     if T[cho[1]][-1] < T[mover][-1] and T[cho[0]][-1] > T[mover][-1]:
#         return cho[0]
#
# temp = T[source].pop()
# T[spare].append(temp)
# lastplayedPos = spare
# while len(T[0]) != 0:
#     base = T[0][-1]
#     while ((sum(range(base + 1)) != sum(T[spare])) + (sum(range(base + 1)) != sum(T[destination]))) != 1:
#         posMove = toMove(lastplayedPos)
#         lastplayedPos = moveWhere(posMove)
#         temp = T[posMove].pop()
#         T[lastplayedPos].append(temp)
