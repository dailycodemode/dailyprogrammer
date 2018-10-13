#
# array = list(range(1,1001)) + [567] + [344]
# array.sort()
#
# for x in range(len(array)-1):
#     if array[x] == array[x+1]:
#         print(x)
#
# ANSWER AND ANALYSIS BY oskar_s
# oskar_s give's 3 possible answers in his answer and gives an explanation why one
# perfroms better than than the previous. I will paraphrase his answer to ensure that I myself
# understand the reasons
#
# # 1
# for i in range(len(array)-1):
#     for j in range(i+1, len(array)):
#         if array[i] == array[j]:
#             print("Duplicate found, array[%d] and array[%d] "
#                   "are both equal to %d" % (i, j, array[i]))
#
# # 2
# array2 = [(v, i) for i,v in enumerate(array)]
# array2.sort()
#
# for i in range(len(array2)-1):
#     if array2[i][0] == array2[i+1][0]:
#         print("Duplicate found, array[%d] and array[%d] are both "
#               "equal to %d" % (array2[i][1], array2[i+1][1], array2[i][0]))
#
# # 3
# hashtable = {}
#
# for i,v in enumerate(array):
#     if v in hashtable:
#         print("Duplicate found, array[%d] and array[%d]"
#               " are both equal to %d" % (hashtable[v], i, array[i]))
#
#     hashtable[v] = i
#
# print("")
#
#
#
# BREAKDOWN
# A hashtable is a data structure which holds key/value pairs i.e. a dictionary in python
#
# If we compare all three methods and determine which one is the fastest then we need to understand how a
# the computer is storing the informataion and how it stores these things.
# But before we do that we'll try to intuitively understand which way is the quikest.
# Well in the first answer there are two nested loops so if you imagine that your repeated numbers are quite high in
# the iteration then it will take a long time to get to it because it has to iterate through every single loop before reaching
# the number. Now the numbers might be low and this could be solved quickly however it's just as likely to be high as it is low
# so image in as somewhere in the middle.
# The second answer sorts the answer first and then iterates through it. So we've asked Python to sort our list for us first
# and then afterwards we'll check what neighbours are beside eachother and then report on that.
# The third answer doesn't bother to perform any sorting instead it checks to see if the number is in the dictionary and if
# not then it stores it as a key, along with its index as its value. We do this so we can find the location of the value in the
# list if we encounter another similar key.
#
# Some questions you might have might be. Isn't checking a dictionary just like checking through a list which you would need to
# iterate over to check if that is has already appeared. The reason that it is different is in the math.
#
#
# SUMMARY
# oskar_s has done a great job at showing us the differnet methods of answering this problem and how to improve perfomrance.
# When I review other peoples code, I am quite familiar with how performance can suffer when the computer get's lost in
# iterating through so many options.