# # ANSWER by DAILY CODE MODE
# array = [4,3,2,1,5,7]
# window = 3
#
# options = []
#
# for x in range(len(array)):
#     if len(array[x:x+3])>2:
#         options.append(array[x:x+3])
#
# answer = []
# for option in options:
#     answer.append(min(option))
#
# print(answer)
#
#
#
# Answer by prophile
# slw=lambda l,w=3:[min(l[n:n+w]) for n in range(len(l)-w+1)]
#
# # BREAKDOWN
# range(len(l)-w+1)
# The reason for this range is to avoid the use of an if statement as one cannot go further than the length of the window
# min(l[n:n+w]
# Gives us our choice window
# It then gets wrapped around in [ ] which will be what slw is equal to.
#
# SUMMARY
# # It's very strange returning to python after a very busy week in VBA which doesn't have the syntax shortening of python so the above answer is really good at getting me back into it.
#
# Fixer
# def window_game(array, window):
#     options = []
#     for x in range(len(array) - window + 1):
#         options.append(min(array[x:x+3]))
#     return options
