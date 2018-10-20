# picture = []
# limit = 5
# for x in range(limit):
#     picture.append([])
#     for y in range(limit):
#         picture[x].append("W")
#
# start = [0,0]
# word = ""
#
# while word != "fin":
#     word = input("do stuff:  ")
#     if word.lower() == 'n': start = [start[0] + 1, start[1]]
#     elif word.lower() == 's': start = [start[0] - 1, start[1]]
#     elif word.lower() == 'e': start = [start[0], start[1] + 1]
#     elif word.lower() == 'w': start = [start[0], start[1] - 1]
#     elif word.lower() == 'stamp': picture[start[0]][start[1]] = "B"
#
# for x in reversed(range(len(picture))):
#     print(picture[x])
#
#
#
# Answer by stgcoder
# import sys
#
# def print_path(w, h, path):
#     grid = [' '] * w * h
#     print(grid)
#     x,y = 0,0
#     for command in path:
#         if command == 'P': grid[x + y*w] = '*'
#         elif command == 'N' : y -= 1
#         elif command == 'S' : y += 1
#         elif command == 'W' : x -= 1
#         elif command == 'E' : x += 1
#
#     for y in range(h):
#         for x in range(w):
#             sys.stdout.write(grid[x + y*w])
#         sys.stdout.write('\n')
#
# print_path(5,5, "PESPESPESPESPNNNNPWSPWSPWSPWSP")
#
# BREAKDOWN
# if command == 'P': grid[x + y*w] = '*'
# Part mutiples by the height by the times and then  added by the width. The reason for doinig this is so that everything can just be kept in a one dimensional array
#
#
# SUMMARY
# I really like the given answer as it just shows the difference between how a normal person and a programmer would think out the situation. Therefore, well done to
