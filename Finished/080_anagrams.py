# # DAILY CODE MODE
# from itertools import permutations
#
# word = "grapes"
#
# perms = [''.join(p) for p in permutations(word)]
#
# words = []
# with open('words.txt','r') as f:
#     for line in f:
#         for word in line.split():
#             words.append(word)
#             if word in perms: print(word)
#
# words.sort(key = lambda s: len(s))
#
# subwords = []
# for x in range(len(words[-1])):
#     subwords.append([z for z in words if len(z) == x])
#
# dicto = {}
# for sub in subwords:
#     for x in range(len(sub)):
#         for y in range(x+1, len(sub)):
#             if sorted(sub[x]) == sorted(sub[y]):
#                 if "".join(sorted(sub[x])) in dicto:
#                     dicto["".join(sorted(sub[x]))] = dicto["".join(sorted(sub[x]))] + 1
#                 else:
#                     dicto["".join(sorted(sub[x]))] = 1
#
# print(dicto.pop(max(dicto, key=dicto.get)))
# print(dicto.pop(max(dicto, key=dicto.get)))
#
#
# Answer by mktange
# [x.strip() for w in [sorted(input("Word:").strip().upper())] for x in open("enable1.txt") if sorted(x.strip().upper()) == w]
#
#
# BREAKDOWN
# As alwayss the easiest way to figure these out is to swap in static values for the most complex pieces of code so here we go;
# [x for w in [sorted("MIKE".strip().upper())] for x in open("enable1.txt") if sorted(x.strip().upper()) == w]
# [x for w in ['E', 'I', 'K', 'M'] for x in open("enable1.txt") if sorted(x.strip().upper()) == w]
#
# .strip()
#  removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns.
# print(sorted("MIKE".strip().upper()))
# This returns a sorted version of the word as an upper case word. It then gets compared against each word in the file (which is given as a generator
#
#
# D = {}
# for w in open("words.txt"):
#     key = ''.join(sorted(w.strip().upper()))
#     if key not in D: D[key] = [w.strip().upper()]
#     else: D[key].append(w.strip().upper())
#
# print(*sorted(D.values(), key=lambda x: len(x), reverse=True)[:2], sep='\n')
#
#
# So the key is each word but rearranged alphabetically. This is done so that every word that enters can be checked
# D[key].append
# A word can be appeneded to a dictionary. I attempted to do this myself but what I did wrong was set it to a list.
# *
# This removes the brackets around a list
# print(*[1,2,3], [4,5,6])
# >>> 1 2 3 [4, 5, 6]
# D.values()
# This returns the values of a dictionary. If we wanted to do the same for keys is input
# D.keys()
# print([1,2,3], [4,5,6], sep='       ')
# >>>[1, 2, 3]       [4, 5, 6]
# sep is a parameter that can be passed through with print which is the seperator. You'd usually use this when you don't want print do not move to the next line
#
# SUMMARY
# I rather enjoyed this question even though I encountered a few problems with. I really enjoyed the given answer too although I'm still a bit confused with some of whata is happening here
# print(*sorted(D.values(), key=lambda x: len(x), reverse=True)[:2], sep='\n')
