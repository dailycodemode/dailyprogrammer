# https://www.reddit.com/r/dailyprogrammer/comments/r59kk/3202012_challenge_28_easy/
# REVIEW OF answer 3 required

array2 = list(range(1, 10))

array2.insert(3,8)
#
# for x in range(len(array)):
#     for y in range(x+1,len(array)):
#         if array[x] == array[y]:
#             print(array[x])
#
# # ANSWER1
# for i in xrange(len(array)-1):
#     for j in xrange(i+1, len(array)):
#         if array[i] == array[j]:
#             print"Duplicate found, array[%d] and array[%d] are both equal to %d" % (i, j, array[i])

# ANSWER2

array2 = [(v, i) for i,v in enumerate(array2)]
array2.sort()

print(array2)
for i in range(len(array2)-1):
    if array2[i][0] == array2[i+1][0]:
        print("Duplicate found, array[%d] and array[%d] are both equal to %d" % (array2[i][1], array2[i+1][1], array2[i][0]))


# ANSWER 3
hashtable = {}
#
# for i,v in enumerate(array):
#     if v in hashtable:
#         print "Duplicate found, array[%d] and array[%d] are both equal to %d" % (hashtable[v], i, array[i])
#
#     hashtable[v] = i
#
# print ""

# BREAKDOWN
# xrange is python2's version of python3's range so I just converted them to that
# in this he also creates a new list from the old with the indexs. A list of tuples
# He does this so that he can point to the location later
# however this have the effect of having to call the first

# SUMMARY
# The first is the same as my own however the second is a neat way of organizing everything in your lists.
