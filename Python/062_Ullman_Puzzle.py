# # DAILY CODE MODE
# arr = [18.1, 55.1, 91.2, 74.6, 73.0, 85.9, 73.9, 81.4, 87.1, 49.3, 88.8, 5.7, 26.3, 7.1, 58.2, 31.7, 5.8, 76.9, 16.5, 8.1, 48.3, 6.8, 92.4, 83.0, 19.6]
# t = 28.2
# n = 3
#
# arr.sort()
# print(sum(arr[:n]) < t)
#
# # Answer by astrosi
# def isSubset(l,t,k):
#     return sum(sorted(l)[:k]) < t
#
#
# # BREAKDOWN
#
# from itertools import combinations
#
# k = 2
# s = [1,2,3,1]
# for x in combinations(s, k):
#     print(x)
# This  was given in another answer which featured this piece I didn't understand.
#
# So combinations will create a number of available unique combinations made up of the values that are passed thorugh to it. So in our list we passed through 1 twice but there is only one combination of this number which combinations is smart enough to recongnize.
#
# SUMMARY
# Pretty much the same answer