# # Answer by DAILY CODE MODE
# first = [1,2,3,4,5]
#
# permutations = []
# for x in first:
#     second = list(first)
#     second.remove(x)
#     for y in second:
#         third = list(second)
#         third.remove(y)
#         for z in third:
#             temp = [x,y,z]
#             temp.sort()
#             if temp not in permutations:
#                 permutations.append(temp)
#
# print(permutations)
#
# # Breakdown
# One thing that can be tricky to keep an eye out for is when
# your lists are pointing to different items. When I first
# wrote my answer I had second = first and thrid = second in
# order to create subsets of my list however the problem with
# doing this is that they were always poinitng to the same
# spot in memory so when I would delete a number from the
# third list, it would delete the same number from the first
# and the seconds lists because they weren't really different
# lists. They were just looking at different things.
# The way to get around this is to tell python that you are
# creating a list out of the previous list instead of just
# assigning to be equal to one another.
# e.g:
# second = list(first)
# # instead of
# second = first
#
# # Answer by baijuke
# def combine(l, n):
#     if n == 1:
#         return [[x] for x in l]
#     out = []
#     for i, elem in enumerate(l):
#         out += map(lambda x: [l[i]] + x, combine(l[i + 1:], n - 1))
#     return out
#
# print(combine([1, 2, 3], 2))
#
# BREAKDOWN
# I always forget about lamba so here's another explanation.
# Lamdas are one off functions which have no name. You will
# declare that you are declaring a function with the
# paratmeters with then the regular semi colon and
# afterwards, the function to be perfomred
#
# lambda x: x + 2
#
# def this_should_really_be_a_lambda(x):
#     return x + 2
#
# If we remember from last week, the map function requires
# two parameters. A function to run and the parameters that
# are to entered in it. The next bit is whewre the real
# work is doing. If youll  remember, we taled about the map
# functino which was a method which woiuld take two arguements
# The function to be passed to it and the array that that
# function will act upon.
#
#
