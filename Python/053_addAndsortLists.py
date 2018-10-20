# # DAILY CODE MODE
# l1 = [1,2,3,4]
# l2 = [2,3,4,5]
#
# sorted(l1 + l2)
#
# # Answer by baijuke
# def merge(s1, s2):
#     i1, i2 = 0, 0
#     while i1 < len(s1) and i2 < len(s2):
#         if s1[i1] > s2[i2]:
#             yield s2[i2]
#             i2 += 1
#         else:
#             yield s1[i1]
#             i1 += 1
#     for x in range(i1, len(s1)): yield s1[x]
#     for x in range(i2, len(s2)): yield s2[x]
#
# from timeit import timeit
# from random import randint
# s1 = sorted([randint(1, 100) for i in range(100)])
# s2 = sorted([randint(1, 100) for i in range(100)])
# print(timeit("merge(s1, s2)", "from __main__ import merge, s1, s2", number=10000))
# print(timeit("sorted(s1 + s2)", "from __main__ import s1, s2", number=10000))
#
# BREAKDOWN
# yield
# Is part of using a generator and which I will explain more in depth when I write about generators
# At the moment, the important thing to remember is that yield is acting similarly to return however the function will pick up where it left off when it runs again
# ie. it will move to i2+=1, because otherwise, the code would never be able to get this far
# from timeit import timeit
# The two initial string statements that are passed into timeit are the statement to be timed and an additional statement used for setup which in our case is
# the function merge and then the two lists s1 and s2
# timeit is a way of measuring very small code snippits. The piece of code that is being written is put into timeit which will time how long the line took to run
# the number part is the amount of executions the code will go through
# [randint(1, 100) for i in range(100)]
# This creates a 100 entry list of random integers between 1 and 100
#
# SUMMARY
# most answers are similar to my own but we're taking a look at the answer to see what is happening.