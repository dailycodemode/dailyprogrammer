# DAILY CODE MODE
# def emirps_below(numbers):
#     for n in range(numbers):
#         if is_prime(n) and is_prime(str(n)[::-1]):
#             if str(n) != str(n)[::-1]:
#                     print(n)
#
#
# def is_prime(n):
#     n = int(n)
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(emirps_below(50))
#
# Answer by PurkinJe90
# import math
# def emirp(num):
#     # Is number and reverse number prime?
#     if (is_prime(num) and is_prime(int(''.join(list(str(num))[::-1])))):
#         if is_palindrome(num):
#             return False
#         else:
#             return True
#     else:
#         return False
#
# def is_prime(num):
#     for i in range(2, int(math.floor(num/2))):
#         if ((float(num)/i)%1 == 0):
#             return False
#         else:
#             pass
#     return True
#
# def is_palindrome(num):
#     num_str = str(num)
#     for i in range(0, int(math.floor(len(str(num))/2))):
#         if num_str[i] != num_str[len(num_str)-i-1]:
#             return False
#     return True
#
# numbers = range(30,100)
# emirps = []
# for num in numbers:
#     if emirp(num):
#         emirps.append(num)
#
# print(emirps)
#
# BREAKDOWN
# int(''.join(list(str(num))[::-1]))
#
# THis is a poor piece of code because it is changing it from one thing into naother and then immediatly changing it back. It would be similar to something like;
# int(str(8))
# The user is first converting the number to a reversed string, splitting it into a list and then joining it all back up before converting it back to a numer. This could all be done with
# int(str(num)[::-1])
#
# SUMMARY
# I prefer my own answer here as I think it is far simpler than the given answer.
#
#
#
