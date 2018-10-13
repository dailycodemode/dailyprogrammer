# # Answer by DAILY CODE MODE
# def fizzBuzz(n):
#     for x in range(1,n+1):
#         if x % 3 == 0 and x % 5 == 0:
#             print("Fizz Buzz")
#         elif x % 3 == 0:
#             print("Fizz")
#         elif x % 5 == 0:
#             print("Buzz")
#         else:
#             print(x)
#
# fizzBuzz(40)
#
# # Answer by ghostdog20
# for i in map(lambda x:(x,'Fizz','Buzz','FizzBuzz')[(x%3==0)+2*(x%5==0)],range(1,input()+1)):print(i)
#
# # BREAKDOWN
# An easy challenge but we are looking at this answer because of how ghostDog wrote
# his answer. I'm not a big fan of these one liners because their is a poor flow to
# them as compared when seperating them out so as impressive as the answer is, I
# would much prefer someone write out something similar to my answer.
#
# when a line ends with :, it means continue writing as if the next writing is on
# a new line
#
# the map function was discussed yesterday but the range function is just setting
# itself up like so
# [1, limit + 1]
#
# lambda expressions are always confusing in python unless you have lots of
# experience with them. they act similarly to the map funciton but in reverse. you
# state what you have and then the colon lets you know what you are to expect
# [(x%3==0)+2*(x%5==0)]
#
# this part is just creataing an index. In python, True and Falses can be added so
# the above is just figuring out what index should be used.
#
# The last bit is in round brackets which means it's in a set. This can be easy to
# forget because we spend so much using square brackets and lists in python. One
# could use square brackets here but because the rules of the game can't change i.e.
# they are immutable, ghostdog20 has used a immutable list which of course would
# be the correct thing to do.
# lambda x:(x,'Fizz','Buzz','FizzBuzz')[(x%3==0)+2*(x%5==0)]
#
# So after all of that, we finally arrive back with our final answer, x. Which is
# either  a number or a string  answer.
#
# # SUMMARY
# # I do like my own answer but the above answer is a really well thought and
# # concise piece of code so the honours have to go to ghostdog20