# # DAILY CODE MODE
# import math
# num = 240
#
# answer = []
#
# for a in range(1, num):
#     for b in range(1, num):
#         # if a ==  115
#         c = math.sqrt(a**2 + b **2)
#         if a + b + c == num:
#             answer.append((a,b,int(c)))
# print(answer)
#
# # Answer by Ttl
# [(504*(j-252)/(j-504),j,-j-(127008)/(j-504)) for j in range(1,504/3) if not (504*(j-252))%(j-504)]
# Breakdwon
# Ttl has quite cleverly rearranged the formula to cut out most of the required computing and reduced processing down to n(0) times.
# The way he has done this is by converting the formulas into a=(2b-n)n/(2(b-n))  and  c = n - a - b.
# (504*(j-252))%(j-504)
# This piece is checking to see if the value returned is divisible by zero.
#
# Summary
# A fab answer as always by Ttl and clearly takes home top boy.