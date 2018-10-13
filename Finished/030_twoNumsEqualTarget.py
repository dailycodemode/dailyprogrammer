# # def will_make_target(target, list):
# #     for x in list:
# #         for y in list:
# #             if x == y:
# #                 pass
# #             elif x + y == target:
# #                 return x,y
# #     return "Uh oh, no way anything will add up to that"
# #
# # print(will_make_target(10, [4,3,2,6]))
#
# num_list = [1, 2, 3, 4, 5]
# target = 6
#
# def checksum(num_list, target):
#     solutions = []
#     solutions.append([(x, y) for x in num_list for y in num_list if x + y == target])
#     return solutions
#
# print(checksum(num_list, target))
# #
# # def find_sum(numbers, target):
# #     for x in numbers:
# #         for y in numbers:
# #             if x + y == target and numbers.index(x) != numbers.index(y):
# #                 return x,y
# #     return None
# #
# # numbers = [1, 2, 3, 4, 5]
# # target = 6
# # print find_sum(numbers, target)
#
# # BREAKDOWN
# # This answere is not correct as it will sum the same number twice however
# # we are using it because it is a good example of going over some python
# # one liners... [one day i'll choose to do them voluntarily]
# # It also returns a double string which is kind of cool.
#
# solutions.append([(x, y) for x in num_list for y in num_list if x + y == target])
#
# [(x, y) for x in num_list for y in num_list if x + y == target]
#
# # so remembering that it is going to perform somehting very similar to what
# # we just wrote.
# # For a python oner, we can put in a nested loop like so
# for x in num_list for y in num_list
# # Then we add the conditional at the end to determine which of the int's we are going to
# #     return
#
# # To get this to work properly, we should have extended the one liner as follows
# # which would have made sure we were not summing a number with itself.
#
# [(x, y) for x in num_list for y in num_list if x + y == target and x != y]
#
# # # SUMMARY
# # I made the same mistake as everyone else and just did two loops
# # without checking if x was equal to why before returning the value
# # So there answer is better because it actually got it right!