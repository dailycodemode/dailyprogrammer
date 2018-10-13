# # Answer by DAILY CODE MODE
# import math
# num = 20
# base = 2
# spaces = int(math.sqrt(num))
# subtotal = num ** (1/base)
# binary = ""
# for x in range(spaces, -1, -1):
#     if base ** x <= subtotal:
#         binary = binary + "1"
#         subtotal -= 2**x
#     else:
#         binary = binary + "0"
#
# # BREAKDOWN
#
# # Answer by xjtian
# def convert_radix(n, r):
#     return get_digit(n) if n < r else convert_radix(n/r, r) + get_digit(n%r)
#
# def get_digit(n):
#     return str(chr(55+n)) if n > 9 else str(n)
#
# print(convert_radix(20, 2))
#
# Breakdown
# A wonderful answer for a challenge which I really struggled with this one. The answer is broken into two parts, the  easier is understnad is the second part
# str(chr(55+n)) if n > 9 else str(n)
# This function will be the last thing that is called but if the number is low enough then it is the first thing that is called.
# Remeber that anything to a base with letters is just a substitution for numbers so instead of saying 11 or 12 which would get really confusing, we say a or b.
# So what this function is doing is checking if the value is over 9 and if so converts it to the appropriate letter.
#  The first function is easiest to understnad by checking out the part that will be used the most which is the recursive element of the call.
# convert_radix(n/r, r) + get_digit(n%r)
# We try and do this with a base 2 example because it is the easiest. And because we are working with recursion, it helps to think of the easiest use of it i.e. it only getting called once
# So if we took the number 2 which in binary is 10, we would send
# n/r ,  r   i.e. 2/2 , 2   back into the funcitno
# This would be small enough to get sent to get the digits which would return back with "1".
# When it is return, the second part of the forumula fires which is get_digit again which is the modulo 0.
# The easiest way of imagining all of this happening is by imagining the cells being filled in from left to right.
#
# SUMMARY
# i wasn't able to get the answer for the second part but I must say that the answer as given by xjtian is superb and is one of the best answers i have ever encountered on Daily Programmer.
