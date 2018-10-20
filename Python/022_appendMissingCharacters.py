# # https://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/
# list1, list2 = ["a","b","c",1,4,], ["a", "x", 34, "4"]
#
# # MINE
# def append_list(list1, list2):
#     for c in list2:
#         if c not in list1: list1.append(c)
#     return list1
#
#
# # ANSWER by idliketobeapython
# def append_unique(a, b):
#     return a + [item for item in b if item not in a]
#
# # BREAKDOWN
# a + [item for item in b if item not in a]
# # is our first list and everything after that it just another line being added on
# paul = [item for item in list2]  # except we don't want all of
#                                 # list2 so we add a conditional
# paul = [item for item in list2 if item not in list1]
#
# SUMMARY
# i've started to notice that one liners are are a very popular thing
# to do in python and it is a mark of ability to be able to achieve them
# The answer is neat and short. The only difference I would make is changing
# the variable names however, this was likely done to keep it neat.