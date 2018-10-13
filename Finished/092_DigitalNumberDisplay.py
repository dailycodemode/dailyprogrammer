# DAILY CODE MODE
# w = 4
# horz = ["+" + "-" * w + "+"]
# vertL = ["|" + " " * w + " "]
# vertR = [" " + " " * w + "|"]
# vertD = ["|" + " " * w + "|"]
#
# two = horz + vertR * w + horz + vertL * w + horz
# five = horz + vertL * w + horz + vertR * w + horz
# three = horz + vertR * w + horz + vertR * w + horz
# six = horz + vertL * w + horz + vertD * w + horz
# for x in range(w * 2 + 3):
#     print(five[x], three[x], six[x], two[x])
#
# Answer by Gix
# numbers = [
# "+---+\n|   |\n|   |\n|   |\n+---+",
# " | \n | \n | \n | \n | ",
# "+---+\n    |\n+---+\n|    \n+---+",
# "+---+\n    |\n  --+\n    |\n+---+",
# "|   |\n|   |\n+---+\n    |\n    |",
# "+---+\n|    \n+---+\n    |\n+---+",
# "+---+\n|    \n+---+\n|   |\n+---+",
# "+---+\n   / \n  /  \n /   \n/    ",
# "+---+\n|   |\n+---+\n|   |\n+---+",
# "+---+\n|   |\n+---+\n    |\n+---+"
# ]
#
#
# x = [line.split('\n') for line in numbers]
# num = [i for i in map(int, input())]
#
# for i in range(5):
#     for n in num:
#         print(x[n][i], end = ' ')
#     print()
#
# BREAKDOWN
# print([i for i in map(int, input())])
# This creates a list of numbers. Inputs are taken in as a string and must be an integer
#
# line.split('\n')
# this splits on a new line
#
# SUMMARY
# Meh, either answer is fine.
