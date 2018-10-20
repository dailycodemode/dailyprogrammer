# DAILY CODE MODE
# word_dict = {}
# with open('slate.txt','r') as f:
#     for line in f:
#         for word in line.split():
#             if word not in word_dict:
#                 word_dict[word] =1
#             else:
#                 word_dict[word] = word_dict[word] + 1
# zipper = list(zip(list(word_dict.keys()), list(word_dict.values())))
# zipper.sort(key=lambda x: x[1], reverse=True)
# print(zipper)
#
# # Answer by _Daimon_
# import re
# import operator
#
# def words(filename, limit):
#     with open(filename, "r") as fil:
#         text = fil.read()
#         words = re.findall("\\b\\w+\\b", text.lower())
#         word_frequency = {}
#         for word in words:
#             word_frequency[word] = word_frequency.get(word, 0) + 1
#         return sorted(word_frequency.iteritems(),
#                       key=operator.itemgetter(1), reverse=True)[:limit]
# 
# BREAKDOWN
# word_frequency.get(word, 0)
# This is a more official way of setting values in a dictionary. The second arguement 0 returns the first value but is not necessary as the dictionary value is a number and not a list
#
# word_frequency.iteritems(),
# This is used to iterate over keys and values in a dictionary by returning a list of dictionary's key/ value pairs as tuples. This was the pytho 2 method of calling the .items method
#
# SUMMARY
# Very similar answers but the last bit was better in the answer as I when I have to return values from a dictionary in some type of sorted list then I usually struggle with what the best way to do this. I'll try to implemenet the given method in future.
