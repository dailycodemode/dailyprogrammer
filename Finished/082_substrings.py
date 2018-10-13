# DAILY CODE MODE
# def substrings(upto):
#     print("Number of available combos: ", sum([x for x in range(1, upto + 1)])) # Bonus 1
#     unique = set()
#     for num in range(97, 96 + upto + 1):
#         ans = ""
#         for z in range(num, 96 + upto + 1):
#             ans = ans + chr(z)
#             if ans not in unique: # Bonus 2
#                 print(ans)
#                 unique.add(ans)
#
# substrings(6)
#
# # Answer by mktange
# alph = "abcdefghijklmnopqrstuvwxyz"
# def substrings(n): return [alph[s:e] for s in range(n) for e in range(s+1,n+1)]
# def bonus1(n): return (n+1)*n//2
# def bonus2(n, string=alph):
#     return [string[s:e] for s in range(n) for e in range(s+1,n+1) if string.find(string[s:e]) == s]
# n = 3
# answer = [alph[s:e] for s in range(n) for e in range(s+1,n+1)]
#
# print(1)
#
#
# BReakdown
# This part for bonus one (n+1)*n//2 is how your find how many combinatins if something cannot be repeated. I've never understood the math for this but this link here does a great job of explaining it all.
# http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/runsums/triNbProof.html