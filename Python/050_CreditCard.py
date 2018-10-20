#
# # Answer by DAILY CODE MODE
# def perfectCreditCard(CC, L):
#     answer = []
#
#     for i, item1 in enumerate(L):
#         for j, item2 in enumerate(L[i+1:]):
#             if item1 + item2 == CC:
#                 answer.append((i,L.index(item2)))
#     return(answer)
#
# # stinktank
# def findItems(cr):
#    it = [(i + 1, j + 1) for i in range(len(l)) for j in range(i+1, len(l)) if l[i] + l[j] == cr]
#    return ("Solution: %s %s" % it[0]) if it else "No solution"
#
# Breakdown
# Similar to what we've seen before and I origianlly attempted to do this
# but didn't feel comfortable doing this so seeing as I didn't know how
# to give the above answer, let's see what we can do
# it = [(i + 1, j + 1) for i in range(len(l)) for j in range(i+1, len(l)) if l[i] + l[j] == cr]
#
# # The most importnat thing to not is that it is a nested loop which can be done
# range(len(l)) for j in range(i+1, len(l))
# # where the second list is made from the first but skips all
# # the numbers which have already been checked
# if l[i] + l[j] == cr]
# # The if statement is quite standard.
# # Finally, stinktank is returning the human readable index which
# # is probably the correct thing to do
#
# # Summary
# # I like both answers and that every possability will be returned so
# # you can choose the items you want. Obviously the next step is to
# # figure out how to do this with more items which might be fun.