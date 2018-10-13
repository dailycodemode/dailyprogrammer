#
# # DAILY CODE MODE
# ans = []
#
# def Morse(spaces, sofar=''):
#     if spaces >= 2:
#         temp = Morse(spaces -2, sofar + '-')
#         if temp != None: ans.append(temp)
#         temp = Morse(spaces -1, sofar + '.')
#         if temp != None: ans.append(temp)
#     elif spaces == 1:
#         print(sofar + '.')
#         return sofar + '.'
#     else:
#         if sofar != None: return sofar
#
# Morse(4)
#
# # while None in ans:
# #     ans.remove(None)
# print(ans)
#
#
# import sys
#
# def morse(size, sequence="", sequences=[]):
#     if size:
#         morse(size-1, sequence+".", sequences)
#         if size >= 2:
#             morse(size-2, sequence+"-", sequences)
#     else:
#         sequences.append(sequence)
#     return sequences
#
# sequences = morse(2)
# map(lambda x: sys.stdout.write(x+' '), sequences)
# print(len(sequences))
#
#
# # BREAKDOWN
#
#
# SUMMARY
# This was my first soiree into recursion and as always I just don't like it all that much because it is hard to see what is happening. In my answer for instance, the value of None is getting returned with my answers so I have to loop through to remove these which I shouldn't need to do. However, because it is recursion then it is very difficult to determine at what step the recursion is happening at.
#
# I also made a mistake when I first attempted this problem as I thought it was much simpler. I thought it only wanted the permutations.
# DAILY CODE MODE
# import itertools
#
# x = ['.', '-']
# [" ".join(p) for p in itertools.product(x, repeat=5)]
# Overall though, I'm glad that I got this one out because the first time you do something is the hardest and I know at some point in the future I will figure out where this recursion problem is arising from.