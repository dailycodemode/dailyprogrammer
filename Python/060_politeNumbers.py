# array = [1, 1, 5, 4, 1, 5, 4, 3, 17, 2, 3, 4, 5, 3, 6, 3, 3]
#
# def good_mannered_numbers(array):
#     for i in range(len(array)-1):
#         target = array[i]
#         summer = 0
#         if array[i] > array[i+1]:
#             count = 1
#             while summer < target:
#                 summer += array[i+count]
#                 count += 1
#             if summer == target:
#                 print(array[i], array[i+1:i+count])
#
# good_mannered_numbers(array)
#
# Answer by prophile
# def polite_configurations(n):
#     from math import sqrt
#     for i in range(int(sqrt(8*n + 1) - 1) // 2, n):
#         try:
#             b_f = 0.5 * (1.0 + sqrt( f4*i*i + 4*i - 8*n + 1))
#             lower, upper = int(b_f), int(b_f + 1.0)
#             if i*(i+1)//2 - lower*(lower-1)//2 == n:
#                 yield range(lower, i + 1)
#             elif i*(i+1)//2 - upper*(upper-1)//2 == n:
#                 yield range(upper, i + 1)
#         except ValueError:
#             # the sqrt threw, meaning 8n > 4i^2 + 4i + 1
#             # this can happen for large n, just continue
#             continue
#
# print(polite_configurations(3))
#
# SUMMARY
# The maths of this was lost on me and after looking into polite numbers; I'm still struggeling to understand what range(int(sqrt(8*n + 1) - 1) // 2, n) is meant to be doing.