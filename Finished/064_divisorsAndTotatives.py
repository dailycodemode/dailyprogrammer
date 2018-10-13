# DAILY CODE MODE
# def divisors(n):
#     return [x for x in range(1, n + 1) if n % x == 0]
#
# def non_divisors(n):
#     return [x for x in range(1, n + 1) if not n % x == 0]
#
#
# def is_prime(a):
#     return all(a % i for i in range(2, a))
#
# def totative(n):
#     div_list = non_divisors(n)
#     ans = [1]
#     for x in div_list:
#         if is_prime(x):
#             ans.append(x)
#     return ans
#
# num = 60
#
# div_list = divisors(num)
# sum_div_list = sum(divisors(num))
# len_divList = len(divisors(num))
# totatives = totative(num)
# totient = sum(totative(num))
#
#
# # Answer by xjtian
# from math import sqrt
#
# def get_divisors(n):
#     divisors = []
#     for i in range(1, int(sqrt(n)) + 1):
#         if n%i == 0:
#             divisors.append(i)
#             divisors.append(n / i)
#     return divisors
#
# def number_of_divisors(n):
#     return len(get_divisors(n))
#
# def sum_of_divisors(n):
#     return sum(get_divisors(n))
#
# def get_totatives(n):
#     totatives = []
#     for i in range(1, n):
#         if gcd(n, i) == 1:
#             totatives.append(i)
#     return totatives
#
# def get_totient(n):
#     return len(get_totatives(n))
#
# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)
#
# print(get_totatives(10))
#
# BREAKDOWN
# In get_divisors, he gets the square root of n where each of these values in the range up to the ceiling of that number will be a factor of that number which I don't understand the reason for dsoing this or the mathematical reasoning behind this
# as in the line after it, he just checks if that i value is divisible of the greater value. I can see why it is faster; instead of looping through the whole number, you only need to loop the root of the number
# I've no real idea what gcd is doing. All that I can see is thata if the value is divible into the larger number and then the modulus is equal to zero then return that value i.e. it
# It's a really nice answer
# Summary
# I hated this question and for something as I recognize as such an easy question, it took me ages to get the correct answer hence why this answer is appearing so far after the answers that I gave before
