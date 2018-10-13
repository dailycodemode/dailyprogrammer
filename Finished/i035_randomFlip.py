# DAILY CODE MODE
# def flip(n):
#     def is_prime(a):
#         return all(a % i for i in range(2, a))
#
#     limit = n
#     answer = {}
#     for x in range(limit + 1):
#         answer[x] = 0
#
#     for x in range(20010):
#         if x> 2000:
#             import time
#             if is_prime(x):
#                 try:
#                     millis = int(str(time.time() % x)[2:3])
#                     if millis <= limit and millis >= 0:
#                         answer[millis] = answer[millis] + 1
#                 except:
#                     pass
#
# print(flip(6))
#
#
#
# # Answer by eruonna
# random(N):
#   let k = ceiling(lg(N))
#   let r = 0
#   repeat k times:
#     r <- 2*r + flip()
#   if r >= N then return random(N)
#   return r
#
# # BREAKDOWN
# i had to look this up because i was not sure of logarithmics since my schooling days
# import math
# print(math.ceil(math.log(17, 2)))
# log 2 is the square root of something and if it does not go evenly then it rounds it to an interger
#
# <-
# This is the R method of saying 'assign to'. In fairness, it makes it much easier to see what is being assigned to, however, the keyboard shortcut is too cumbersome
# for something so finicky. It's really a matter of preference.
#
# 'random' gets sent in with the limit N. This gets rounded up after square rooting. So if we are taking 6 then
# As for the log2 of N, I think this is used to limit the for loop as anything past the square root of an iterator can't be used.
#
# Then k = 3
# Looping 2 times, r is assigned to twice itself + random choice between 1 and 0. It starts at 0 so doing this will double r and then add a number to it
#
# It can be a little confusing as to why this is happening becasue it doesn't seem that the math is correct. To come up a zero it would require three 0 flips which would be .5 * .5 * .5 = 1/8
# as for a one it would be the same odds i.e. .5 * .5 * .5 = 1/8 which are the same odds. Working are way up we can see that there is only one way of getting each combination of that number.
# So what do we do when the number flips and we get a 6 or 7? Well, we head back into the same function and do it all again until we do get the allowable answer.
# Once it gets large enough it get's sent back allows recursion into itself with the same N number. I'm guessing the reason for this is that we can't return a
# a value higher than itself so it gets sent back in and repeats the process until a number less than 6 is chosen.
#
# How is this to work though as r will return 0 immediatly
#
# COMMENT
# My answer is garbage and it just tries to do something to get a random number however looking back on it all, I can barely understand what I was even attempting myself.
# As for the answer, these questions are really helping me to think more like a mathematician and hopefully I can work through all these less commonly known methods to getting such an answer with time.
