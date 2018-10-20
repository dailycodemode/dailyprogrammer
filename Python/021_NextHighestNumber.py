# #  MINE
# import itertools
# input = "1234"
# x = itertools.permutations(input, 4)
# numbers = []
# for y in x:
#     numbers.append(list(y))
#
# arr_numbers = []
# for number in numbers:
#     arr_numbers.append("".join(number))
# arr_numbers.sort()
#
# next_num_loc = arr_numbers.index(input) + 1
#
# print(arr_numbers[next_num_loc])
#
# # ANSWER by Should_I_say_this
# def n(num):
#     from itertools import permutations
#     numb = str(num)
#     for i in sorted(permutations(str(numb))):
#         b = int(''.join(i))
#         if b> int(numb):
#             print(b)
#             break
#
# n(1234)
#
# BREAKDOWN
# Another question which has a few interesting pieces. Honesty, this question abslutely killed me. i was not aware of the the itertools - permutations library, and tried to build it
# myself from scratch

# sorted(permutations(str(numb))
#
# # let's make this easier to understand and switch it to something simple like
# permutations("28")
# >>> [("2", "8"), ("8", "2")]
#  # this will return all permutations of the number that you entered and return each permutation as a tuple.
#  # the sorted bit will just sort all of our values from lowest to highest.
#
# b = int(''.join(i))
#              # here he creates a new variable 'b' instead of changing the value i because i is immutable i.e. can't be changed
#
#              SUMMARY
# not too different to what i initially attempted however I was having trouble getting the tuples to act the way I wanted
# so created a list out of them which was probably not necessary
#
#
