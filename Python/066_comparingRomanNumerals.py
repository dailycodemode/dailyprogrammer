# DAILY CODE MODE
# def is_X_bigger_than_Y(x,y):
#     l = len(max([x,y], key=len))
#     for ind in range(l):
#         if ord(x[ind]) == ord(y[ind]):
#             pass
#         elif ord(x[ind]) >= ord(y[ind]):
#             return True
#         elif ord(x[ind]) <= ord(y[ind]):
#             return False
#
#
#
# Answer by loonybean
# import re
#
# def compareRoman(x,y):
#     countCharsX, countCharsY = [len(re.findall(c,x)) for c in 'MDCLXVI'], [len(re.findall(c,y)) for c in 'MDCLXVI']
#     for i in range(0, 7):
#         if countCharsX[i] != countCharsY[i]:
#             return True if countCharsX[i] < countCharsY[i] else False
#     return False
#
# BREAKDOWN
# countCharsX = [len(re.findall(c,'XIII')) for c in 'MDCLXVI']
# >>> [0, 0, 0, 0, 1, 0, 3]
# This is a very nice piece of code which breaks the string into a list where each count of that in the list appears.
# As usual, lets split this apart to see what is happening
#
# for c in 'MDCLXVI'
# this is creating a generator where each character will be sent into our regular expression. For simplicity, let's make it much smaller so that we can focus on everything else
#
# countCharsX = [len(re.findall(c,'XIII')) for c in 'I']
# # So what we can see now is that we are trying to find how often "I" is appearing in the string
#
# #Let's see what will happen when we remove the len part which will just give us lists with a list, showing the number  of appearances of each character
# countCharsX = [re.findall(c,'XIII') for c in 'I']
# >>> [['I', 'I', 'I']]
#
# Finally, the answer iterates over the answer and then checks the count of each number against each other. When one is finally bigger than the other, it will pick which one is bigger
#
# SUMMARY
# Great challenge, and a lovely one to think about. Lovely answer.
